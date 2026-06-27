# Catalog Architecture

Версия: 1.0

---

## Назначение

Документ описывает архитектуру каталога HAUSPELLA.

Каталог является общей частью платформы и используется как HAUSPELLA ERP, так и HAUSPELLA Shop.

## Структура каталога

```text
Catalog
│
├── Category
├── Product
│
├── ProductImage
├── ProductDocument
├── ProductVideo
└── ProductRichContent
```


## Product Media

Все медиафайлы товара являются отдельными сущностями и принадлежат модели Product.

Каждый тип медиа решает свою задачу и хранится независимо от остальных.


```text
Product
│
├── ProductImage
├── ProductDocument
├── ProductVideo
└── ProductRichContent
```



---

# Product Media

Назначение:

Подсистема хранения мультимедийного контента товаров.

Структура:

Product
│
├── ProductImage
├── ProductDocument
└── ProductVideo
    │
    └── ProductVideoSource


## ProductVideo

Логическое видео товара.

Не содержит информацию о платформе размещения.

Примеры:

- Обзор товара
- Инструкция
- Распаковка
- Сборка
- Обслуживание

Один товар может содержать неограниченное количество логических видео.

---

## ProductVideoSource

Источник публикации логического видео.

Содержит ссылку на размещённое видео.

Примеры платформ:

- YouTube
- VK Видео
- Rutube
- Vimeo

Одно логическое видео может иметь неограниченное количество источников публикации.