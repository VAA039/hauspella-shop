from django.db import models

from .product_video import ProductVideo


class VideoPlatform(models.TextChoices):
    """
    Платформа размещения видео.
    """

    VK_VIDEO = "vk_video", "VK Видео"
    RUTUBE = "rutube", "Rutube"
    DZEN_VIDEO = "dzen_video", "Дзен Видео"
    PLATFORMA = "platforma", "Платформа"
    ODNOKLASSNIKI = "ok_video", "Одноклассники Видео"
    KINESCOPE = "kinescope", "Kinescope"
    WIBES = "wibes", "Wibes"
    RAMBLER = "rambler", "Рамблер"
    COUB = "coub", "Coub"
    TWITCH = "twitch", "Twitch"

    OTHER = "other", "Другое"


class ProductVideoSource(models.Model):
    """
    Источник публикации видео товара.

    Одно логическое видео может иметь несколько источников публикации
    на различных видеоплатформах.
    """

    video = models.ForeignKey(
        ProductVideo,
        verbose_name="Видео",
        on_delete=models.CASCADE,
        related_name="sources",
    )

    platform = models.CharField(
        verbose_name="Платформа",
        max_length=30,
        choices=VideoPlatform.choices,
    )

    url = models.URLField(
        verbose_name="Ссылка",
        max_length=500,
    )

    sort_order = models.PositiveSmallIntegerField(
        verbose_name="Порядок",
        default=0,
        help_text="Чем меньше число, тем выше источник в списке.",
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )


    class Meta:
        verbose_name = "Источник видео"
        verbose_name_plural = "Источники видео"
        ordering = (
            "sort_order",
            "id",
        )

        constraints = [
            models.UniqueConstraint(
                fields=("video", "platform"),
                name="unique_product_video_platform",
            ),
        ]

    def __str__(self):
        return f"{self.get_platform_display()} — {self.video.title}"