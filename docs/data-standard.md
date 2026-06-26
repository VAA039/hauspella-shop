# HAUSPELLA Data Standard

Версия: 1.0

---

## Назначение

Документ определяет единый стандарт хранения данных для всех проектов платформы HAUSPELLA.

Все новые сущности должны соответствовать данному стандарту.

---

# Общие правила

- Один объект — одна ответственность.
- Имена полей всегда на английском языке.
- Snake_case для всех полей.
- Все даты оканчиваются на `_at`.
- Все логические поля начинаются с `is_`.
- Все URL оканчиваются на `_url`.
- Все HTML-поля оканчиваются на `_html`.
- Все PDF-файлы оканчиваются на `_pdf`.

---

# Product

## Identity

| Поле | Тип | Описание |
|------|-----|----------|
| article | CharField | Внутренний артикул HAUSPELLA |
| name | CharField | Название товара |
| slug | SlugField | URL товара |
| category | ForeignKey | Категория |

---

## Commerce

| Поле | Тип | Описание |
|------|-----|----------|
| price | Decimal | Цена |
| old_price | Decimal | Цена до скидки |

---

## Content

| Поле | Тип | Описание |
|------|-----|----------|
| short_description | Text | Краткое описание |
| description | Text | Полное описание |

---

## SEO

| Поле | Тип | Описание |
|------|-----|----------|
| seo_title | CharField | SEO Title |
| meta_description | Text | Meta Description |
| main_keyword | CharField | Главный поисковый запрос |
| search_aliases | Text | Дополнительные поисковые запросы |

---

## Marketing

| Поле | Тип | Описание |
|------|-----|----------|
| review_analysis | Text | Анализ отзывов конкурентов |
| unique_selling_points | Text | Уникальные преимущества товара |
| customer_pain_points | Text | Основные боли покупателей |
| advantages | Text | Преимущества товара |

---

## Media

| Поле | Тип | Описание |
|------|-----|----------|
| video_url | URLField | Ссылка на видео |
| rich_content_html | Text | HTML Rich Content |
| manual_pdf | FileField | Инструкция пользователя |

---

## Service

| Поле | Тип | Описание |
|------|-----|----------|
| is_active | Boolean | Активность товара |
| created_at | DateTime | Дата создания |
| updated_at | DateTime | Дата изменения |