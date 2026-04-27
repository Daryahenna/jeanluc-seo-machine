# Claude — инструкция для работы с этим репо

Если ты работаешь с этим репо как AI-агент (Claude, opencode, Cursor, etc.), читай это в первую очередь.

## Что это за проект

SEO-машина для Jean-Luc Médéric — статический контент-хаб на Jekyll + GitHub Pages. Гонит органический трафик на главный сайт `jeanlucmederic.site` через long-tail SEO-гайды по продажам. Тематика: продажи по методу Michael Bang "Golden Key of Sales".

Live: https://daryahenna.github.io/Jean-Luc-Mederic/ru/guides/

## Перед любой работой над статьёй (`_guides/`)

**Обязательно прочитай** [`prompts/style-guide-jlm.md`](prompts/style-guide-jlm.md) — там вся методология: тон, структура, frontmatter, дизайн-система (HTML-классы), длина, SEO-чеклист, workflow публикации, anti-patterns.

Без этого ты будешь повторять ошибки прошлых итераций (TL;DR в начале, разорванные `<a>`, вы вместо ты, дублирование FAQ, и т.д.).

Эталон стиля — `_guides/ru/objection-dorogo.md`. По нему сверяй любую новую или переписываемую статью.

## Перед поиском новых тем

Используй промпт из [`prompts/ru-topic-researcher.md`](prompts/ru-topic-researcher.md). Он находит реальные запросы клиентов на форумах + сверяет с Wordstat. **Не выдумывай темы из головы.**

## Workflow публикации

Подробно в style-guide. Кратко: clone в `/tmp/jlm`, edit, parallel-copy в mount для GitHub Desktop у Даши, commit, push. Прямой коммит из mount-папки не работает — GitHub Desktop держит lock на `.git`.

## Что НЕ трогать

- `https://jeanlucmederic.site/` — главный сайт. Принципиально не подключаемся к нему и не модифицируем (защита от Google penalties за automation footprint).
- `extracted/` — это сырьё (тексты Golden Key), не редактируется
- `assets/img/banner-paris-*.png` — баннеры мастер-класса с готовым текстом

## Вопросы / решения, уже зафиксированные

- **Многоязычность:** сейчас RU. FR будет следующим (главный рынок — Франция). EN после.
- **Хостинг и домен:** пока GitHub Pages под `daryahenna.github.io`. Будет переезд на собственный домен (минимум `.com`, желательно `.fr`) перед FR-волной.
- **Тон:** Medium-style на «ты», личный голос, реальные диалоги. Никакого канцелярита.

См. также `SESSION.md` для текущего состояния и истории решений.
