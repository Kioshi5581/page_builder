from django.db import models


class Homepage(models.Model):
    slug = models.SlugField(max_length=200)
    page_title = models.CharField(max_length=200)
    page_keywords = models.CharField(max_length=500)
    page_desc = models.TextField()
    hero_h1 = models.CharField(max_length=200)
    hero_h2 = models.CharField(max_length=200)
    hero_table = models.CharField(max_length=200)
    hero_item1 = models.CharField(max_length=200)
    hero_item2 = models.CharField(max_length=200)
    hero_item3 = models.CharField(max_length=200)
    hero_item4 = models.CharField(max_length=200)
    hero_item5 = models.CharField(max_length=200)
    hero_item6 = models.CharField(max_length=200)
    hero_item7 = models.CharField(max_length=200)
    hero_item8 = models.CharField(max_length=200)
    hero_item9 = models.CharField(max_length=200)
    href_btn = models.CharField(max_length=200)
    hero_price = models.IntegerField()
    hero_image = models.ImageField(upload_to="hero")
    about_h1 = models.CharField(max_length=200)
    about_p = models.TextField()
    about_h2 = models.CharField(max_length=200)
    why_pawnhost_title = models.CharField(max_length=200)
    why_pawnhost_image = models.ImageField(upload_to="why_pawnhost")
    why_pawnhost_h1 = models.CharField(max_length=200)
    why_pawnhost_p = models.TextField()
    feature_section_title = models.CharField(max_length=200)
    reviews_section_title = models.CharField(max_length=200)
    transfer_website_image = models.ImageField(upload_to="transfer_website")
    
    transfer_website_title = models.CharField(max_length=200)
    transfer_website_desc = models.TextField()
    transfer_website_href = models.CharField(max_length=200)

    def __str__(self):
        return self.slug
    

class Servers(models.Model):
    slug = models.SlugField(max_length=200)
    page_title = models.CharField(max_length=200)
    page_keywords = models.CharField(max_length=500)
    page_desc = models.TextField()
    hero_h1 = models.CharField(max_length=200)
    hero_h2 = models.CharField(max_length=200)
    hero_p = models.TextField()
    servers_title = models.CharField(max_length=200)
    payments_options = models.CharField(max_length=500)
    hero_title = models.CharField(max_length=200)
    table_title = models.CharField(max_length=200)
    table_title2 = models.CharField(max_length=200)
    table_title3 = models.CharField(max_length=200)
    table_title4 = models.CharField(max_length=200)
    feature_section_title = models.CharField(max_length=200)
    feature_section_desc = models.TextField()
    feature_section_btn_href = models.CharField(max_length=200)
    feature_section_img = models.ImageField(upload_to="feature_section")


    def __str__(self):
        return self.slug




class pricing_table(models.Model):
    table_title = models.CharField(max_length=200)
    table_feature1 = models.CharField(max_length=200)
    table_feature2 = models.CharField(max_length=200)
    table_feature3 = models.CharField(max_length=200)
    table_feature4 = models.CharField(max_length=200)
    table_feature5 = models.CharField(max_length=200)
    table_feature6 = models.CharField(max_length=200)
    table_feature7 = models.CharField(max_length=200)
    table_feature8 = models.CharField(max_length=200)
    table_feature9 = models.CharField(max_length=200)
    table_feature10 = models.CharField(max_length=200)
    table_price = models.IntegerField()
    table_href = models.CharField(max_length=200)

    def __str__(self):
        return self.table_title


class call_to_action(models.Model):
    img = models.ImageField(upload_to="call_to_action")
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.title


class review(models.Model):
    image = models.ImageField(upload_to="reviews")
    text = models.TextField()
    credit = models.CharField(max_length=200)

    def __str__(self):
        return self.credit
 