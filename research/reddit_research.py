"""
Reddit Research Agent — Jean-Luc SEO Machine
Ищет живые цитаты продажников по заданным темам.

Установка зависимостей:
    pip install praw

Запуск:
    python reddit_research.py
"""

import praw
import json
from datetime import datetime

# ── Credentials ──────────────────────────────────────────────────────────────
CLIENT_ID     = "kd4XRoZMN0h9gaYITb5LFQ"
CLIENT_SECRET = "93i8shGx2u_HxxLEufQjAAmt1Uaj8Q"
USERNAME      = "Square_Praline_5814"
PASSWORD      = "ВПИШИсвойПАРОЛЬздесь"   # <-- заполни
USER_AGENT    = f"seo-research-bot/1.0 by {USERNAME}"

# ── Subreddits и темы для поиска ──────────────────────────────────────────────
SUBREDDITS = ["sales", "entrepreneur", "smallbusiness", "freelance", "consulting"]

QUERIES = [
    # Возражения
    "too expensive objection",
    "prospect said too expensive",
    "client ghosted after proposal",
    "need to think about it objection",
    "already have a vendor",
    "no budget objection",
    "need to check with my boss",
    # Закрытие
    "closing the deal tips",
    "soft close sales",
    # AI для продаж
    "ChatGPT for sales",
    "AI sales assistant",
    # Mindset
    "fear of selling",
    "hate cold calling",
    "scared to quote price",
]

MIN_SCORE = 5       # минимальный upvote у поста
MIN_COMMENTS = 3    # минимум комментариев
POST_LIMIT = 10     # сколько постов брать на один запрос

# ── Основная логика ───────────────────────────────────────────────────────────

def connect():
    return praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=USERNAME,
        password=PASSWORD,
        user_agent=USER_AGENT,
    )


def search_posts(reddit, query, subreddit_name):
    results = []
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.search(query, sort="top", time_filter="year", limit=POST_LIMIT):
        if post.score < MIN_SCORE or post.num_comments < MIN_COMMENTS:
            continue

        top_comments = []
        post.comments.replace_more(limit=0)
        for comment in post.comments[:5]:
            if len(comment.body) > 30:
                top_comments.append({
                    "author": str(comment.author),
                    "score": comment.score,
                    "body": comment.body[:500],
                })

        results.append({
            "subreddit": subreddit_name,
            "query": query,
            "title": post.title,
            "url": f"https://reddit.com{post.permalink}",
            "score": post.score,
            "num_comments": post.num_comments,
            "selftext": post.selftext[:600] if post.selftext else "",
            "top_comments": top_comments,
            "date": datetime.utcfromtimestamp(post.created_utc).strftime("%Y-%m-%d"),
        })
    return results


def run():
    print("Подключаюсь к Reddit...")
    reddit = connect()
    print(f"Авторизован как: {reddit.user.me()}\n")

    all_results = []

    for subreddit in SUBREDDITS:
        for query in QUERIES:
            print(f"  Ищу [{subreddit}] '{query}'...")
            posts = search_posts(reddit, query, subreddit)
            all_results.extend(posts)
            print(f"    Найдено постов: {len(posts)}")

    # Сохраняем в JSON
    output_file = "reddit_results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

    print(f"\nГотово. Всего постов: {len(all_results)}")
    print(f"Результаты сохранены в: {output_file}")

    # Печатаем топ цитат
    print("\n── ТОП ЦИТАТЫ ──────────────────────────────────────────────")
    for item in sorted(all_results, key=lambda x: x["score"], reverse=True)[:10]:
        print(f"\n[{item['date']}] r/{item['subreddit']} | {item['score']} upvotes")
        print(f"Пост: {item['title']}")
        print(f"URL:  {item['url']}")
        if item["selftext"]:
            print(f"Текст: {item['selftext'][:200]}...")
        if item["top_comments"]:
            c = item["top_comments"][0]
            print(f"Топ комментарий ({c['author']}): {c['body'][:200]}")


if __name__ == "__main__":
    run()
