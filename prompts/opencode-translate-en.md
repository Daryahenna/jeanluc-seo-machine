# Opencode — техзадание на перевод RU → EN

Этот файл — единственный источник правды для перевода гайдов с русского на английский. Ты, opencode (gpt-5.2 или другой агент), читаешь это и действуешь по правилам. Если что-то не покрыто — спроси в чат, не выдумывай.

---

## Миссия

Перевести 8 гайдов из `_guides/ru/` на английский. Создать 8 новых файлов в `_guides/en/`. **Не трогать ни один существующий файл.** Цель — production-ready тексты для глобальной англоязычной аудитории B2B-продажников и предпринимателей.

Тон — `you` (informal direct, как у HubSpot, Salesforce blog, Sahil Bloom). Личный голос автора Jean-Luc Médéric, как тренера-ровесника. Никакого корпоративного жаргона.

---

## ⛔ Жёсткие правила безопасности

1. **Никогда** не модифицируй файлы в `_guides/ru/`. Read-only.
2. **Никогда** не модифицируй `_guides/fr/`, `_layouts/`, `_includes/`, `assets/`, `_config.yml`. Read-only.
3. **Только** создавай новые файлы в `_guides/en/`.
4. Если файл `_guides/en/<slug>.md` уже существует — **пропусти его**, не перезаписывай. Логируй: `SKIPPED: <slug> (already exists)`.
5. Если фраза/идиома не переводится естественно — переведи приблизительно и оставь `<!-- TRANSLATOR NOTE: ... -->` рядом.
6. Не используй переводчики Google/DeepL. Перевод делает только модель напрямую.

---

## Маппинг slug-ов RU → EN

Используй ровно эти slug-и для целевых файлов:

| RU исходник | EN target | Целевой URL |
|---|---|---|
| `objection-dorogo.md` | `objection-its-too-expensive.md` | `/en/guides/objection-its-too-expensive/` |
| `objection-podumat.md` | `objection-let-me-think.md` | `/en/guides/objection-let-me-think/` |
| `objection-pozhe.md` | `objection-not-now.md` | `/en/guides/objection-not-now/` |
| `objection-net-vremeni.md` | `objection-no-time.md` | `/en/guides/objection-no-time/` |
| `objection-nado-posovetovatsya.md` | `objection-need-to-consult.md` | `/en/guides/objection-need-to-consult/` |
| `closing-questions.md` | `closing-questions.md` | `/en/guides/closing-questions/` |
| `prospecting-plan.md` | `prospecting-plan.md` | `/en/guides/prospecting-plan/` |
| `kp-ghosting.md` | `client-ghosted-after-proposal.md` | `/en/guides/client-ghosted-after-proposal/` |

---

## Заголовки EN (для `title` в frontmatter)

Естественные поисковые запросы, как реальный B2B-продажник из США/UK их искал бы.

| RU title | EN title |
|---|---|
| « Дорого » — как ответить, чтобы клиент не сорвался | "It's too expensive" — how to respond without losing the deal |
| « Мне надо подумать » — что отвечать, чтобы клиент не пропал | "Let me think about it" — how to stop the client from disappearing |
| « Давайте позже » — что отвечать, чтобы клиент не ушёл к конкуренту | "Let's revisit later" — how to keep the deal alive when the client stalls |
| « Нет времени » — что отвечать, чтобы не звучать навязчиво | "I don't have time" — how to respond without sounding pushy |
| « Мне надо посоветоваться » — как не потерять сделку в чужих руках | "I need to consult with someone" — how to not lose the deal in someone else's hands |
| Закрытие сделки без давления — 3 типа вопросов, которые работают | Closing deals without pressure — 3 types of questions that work |
| План проспектинга — 5 каналов, которые дают стабильный поток лидов | Prospecting plan — 5 channels that deliver a steady lead flow |
| « Клиент пропал после КП » — что писать и когда звонить, не выбешивая | "Client ghosted after the proposal" — what to write and when to call, without being annoying |

---

## Frontmatter — пример обязательного формата

```yaml
---
title: "EN title from the table above"
description: "EN description, ~140-160 chars, with keyword and promise"
promise: "In X minutes you'll have [concrete result] — without [main client fear]."
category: "Objections"        # см. таблицу категорий
chips:
  - "Objections"
  - "Script inside"            # см. chips таблицу
  - "X min read"
hero_emoji: "💸"               # БЕЗ изменений, оставь как в исходнике
hero_caption: "EN translation of caption"
author: "Jean-Luc Médéric"
date: 2026-04-27
reading_time: "X min read"
lang: en                       # ← Замени с ru на en
slug: <slug-en-из-таблицы>     # ← Возьми из таблицы маппинга
faq:                           # Переведи все 4 вопроса и ответы
  - q: "..."
    a: "..."
hreflang_alt:                  # Альтернативные языки
  ru: /ru/guides/<slug-ru>/
  fr: /fr/guides/<slug-fr>/
---
```

### Маппинг категорий

| RU | EN |
|---|---|
| Возражения | Objections |
| Закрытие | Closing |
| Воронка | Pipeline |
| Проспектинг | Prospecting |

### Маппинг chips

| RU фраза | EN фраза |
|---|---|
| Возражения | Objections |
| Закрытие | Closing |
| Скрипт внутри | Script inside |
| Скрипт + диалог | Script + dialog |
| Шаблон + диалог | Template + dialog |
| План + чек-листы | Plan + checklists |
| Проспектинг | Prospecting |
| X мин чтения | X min read |

---

## Правила перевода тела статьи

### Тон и обращение

- **`you`** (informal direct). Always. Это уже стандартный английский для sales/business-content.
- Личный голос. Прямо, без воды. Medium-style.
- Короткие предложения. 1–3 предложения на абзац.
- **Без канцелярита** типа "It is important to note that..." / "In the present article, we will examine..." — пиши как живой человек.
- Активный залог везде, где возможно.

### Терминология (фиксированная)

| RU | EN |
|---|---|
| «Менеджер» (в диалогах) | "Seller" (NOT "Manager", NOT "Salesperson") |
| Клиент | Client |
| Сделка | Deal |
| Проспектинг | Prospecting |
| Возражение | Objection |
| ЛПР | decision-maker (DM) |
| Холодный звонок | cold call |
| Закрытие | Closing |
| Скрипт | script |
| Воронка | pipeline / funnel |
| КП (коммерческое предложение) | proposal |
| Дожать | force a close (avoid in seller's voice — it's anti-pattern) |

### Кавычки

- Стандартные английские: `"text"` (curly quotes `"text"` тоже OK)
- Никаких французских `« »` или русских `«»`

### Цитаты Michael Bang

В RU-исходнике цитата уже на русском (вторичный перевод). Для EN — **верни оригинальный английский**. Bang преподаёт на английском, его выступления — англоязычные. Используй естественный английский, передающий смысл цитаты:

```html
<div class="callout is-quote">
<p class="callout-title">Quote</p>
<p>"Original English quote that conveys the same meaning as the RU version."</p>
<cite>— Michael Bang, lesson #15 "Objection Handling"</cite>
</div>
```

### Цены и валюта

- **Евро остаются евро**: `€18,000` → `€18,000` (Jean-Luc — европейский тренер, цена в евро)
- Сроки: `90 дней` → `90 days`
- Проценты: те же, формат тот же

### Имена и реалии

- `Jean-Luc Médéric` — без изменений
- `Michael Bang` — без изменений
- `Golden Key of Sales` — оставь английское название
- Мастер-класс 9–10 мая в Париже → `May 9-10 Paris masterclass`

### HTML-структура

**Нельзя** менять. Каждый блок исходника соответствует ровно одному блоку перевода:

- `<div class="callout is-key">` ↔ `<div class="callout is-key">`
- `<div class="callout is-tip">` ↔ `<div class="callout is-tip">`
- `<div class="callout is-warn">` ↔ `<div class="callout is-warn">`
- `<div class="callout is-quote">` ↔ `<div class="callout is-quote">`
- `<div class="bad-example">` ↔ `<div class="bad-example">`
- `<div class="good-example">` ↔ `<div class="good-example">`
- `<div class="phrase-card">` ↔ `<div class="phrase-card">`
- `<div class="dialog">` ↔ `<div class="dialog">`
  - `<p class="dialog-line">` (Seller) и `<p class="dialog-line is-them">` (Client) — без изменений
  - Внутри: `<span class="who">Seller:</span><span class="what">text</span>`
- `<ul class="check">` ↔ `<ul class="check">`

### Inline-баннер CTA

В исходнике: `{% include paris-banner.html utm_medium="guide_inline" %}`

В переводе: **точно такая же строка**. Liquid-template сам подхватит `page.lang: en` и подставит английский баннер + UTM с `utm_campaign=en`.

### Внутренние ссылки на другие гайды

Когда видишь в исходнике:
```
[«Надо подумать»]({{ site.baseurl }}/ru/guides/objection-podumat/)
```

Переведи на EN-эквивалент по таблице slug-ов:
```
["Let me think about it"]({{ site.baseurl }}/en/guides/objection-let-me-think/)
```

Если ссылка ведёт на гайд, который ещё не переведён — всё равно ставь EN-ссылку (когда тот гайд переведётся, ссылка заработает).

---

## Validation checklist (выполняй после каждого файла)

После генерации каждого файла `_guides/en/<slug>.md` проверь:

- [ ] Frontmatter содержит все обязательные поля: `title`, `description`, `promise`, `category`, `chips`, `hero_emoji`, `author`, `date`, `reading_time`, `lang: en`, `slug` (EN), `faq` (4 шт), `hreflang_alt`
- [ ] `lang: en` (не `ru`!)
- [ ] `slug` соответствует таблице маппинга
- [ ] Количество HTML-блоков в EN = количество в RU
- [ ] В диалоге используется `Seller:` (НЕ `Менеджер`, НЕ `Manager`, НЕ `Salesperson`, НЕ `Жан-Люк`)
- [ ] Все внутренние ссылки `[...]({{ site.baseurl }}/...)` ведут на `/en/guides/`, не `/ru/guides/`
- [ ] Тон `you` (всегда)
- [ ] Нет следов русского текста (особенно в диалогах, cite, frontmatter)
- [ ] FAQ: 4 вопроса, все переведены
- [ ] Цена `€18,000` или другая — формат сохранён, валюта евро

Если хоть одна галочка не стоит — не помечай файл готовым, добавь `<!-- VALIDATION: ... -->` сверху и переходи к следующему.

---

## Output format и логирование

В конце создай `_guides/en/_TRANSLATION_LOG.md`:

```
# Translation log RU → EN
Date: YYYY-MM-DD
Source commit: <SHA>
Model: <model-name>

## Translated successfully
- objection-its-too-expensive.md (from objection-dorogo.md)
- ...

## Skipped
- <slug> (reason)

## Validation failures (need human review)
- <slug>: <причина>
```

---

## Контекст метода (для понимания)

Все статьи учат методу **Golden Key of Sales** Михаэля Бэнга — 6-шаговый процесс:

1. Prospecting
2. Relationship Building
3. Qualifying
4. Presentation
5. Objection Handling
6. Closing

Если в RU встречается отсылка к этим шагам — используй английские термины из списка.
