from django.contrib import admin
from .models import (
        Category,
        Company,
        Genre,
        GamePlatform,
        Game,
        GameScreenShoots,
        RatingStar,
        Rating,
        Review
)

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Genre)
admin.site.register(GamePlatform)
admin.site.register(Game)
admin.site.register(GameScreenShoots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Review)