class Novel:
    def __init__(self,hero_id,hero_name,hero_title,hero_profession,is_week_free,hero_keywords,hero_url,hero_alias):
        self.hero_id = hero_id,
        self.hero_name = hero_name,
        self.hero_title = hero_title,
        self.hero_profession = hero_profession,
        self.hero_img_url_big =f"https://game.gtimg.cn/images/lol/act/img/skin/big_{ hero_id }.jpg",
        self.hero_img_url_small = f"https://game.gtimg.cn/images/lol/act/img/skinloading/{ hero_id }.jpg",
        self.is_week_free = is_week_free,
        self.hero_keywords = hero_keywords,
        self.hero_url = hero_url,
        # 英雄别名
        self.hero_alias = hero_alias
        self.hero_alias_temp = self.hero_alias.lower()
        self.hero_detail_url = f"https://yz.lol.qq.com/v1/zh_cn/champions/{self.hero_alias_temp}/index.json",


class HeroStory:
    def __init__(self,hero_title,hero_name,hero_image,hero_image_big,hero_quote,hero_short,hero_full,hero_related):
        self.hero_title = hero_title,
        self.hero_name = hero_name,
        self.hero_image = hero_image,
        self.hero_image_big = hero_image_big,
        self.hero_quote = hero_quote,
        self.hero_short = hero_short,
        self.hero_full = hero_full,
        self.hero_related = hero_related