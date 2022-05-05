from modeltranslation.translator import register, TranslationOptions
from .models import Transport


@register(Transport)
class TransportTranslationOptions(TranslationOptions):
    fields = ('description',)