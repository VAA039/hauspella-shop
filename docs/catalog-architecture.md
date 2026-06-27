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