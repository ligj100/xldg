from django.db import models


# Create your models here.
# 用于记录平台信息，比如淘宝、京东等
class t_lm_pt(models.Model):
    pt_id: int = models.AutoField(primary_key=True)
    pt_bm = models.IntegerField()
    pt_mc = models.CharField(max_length=20)
    pt_url = models.URLField()
    pt_created = models.DateField()


# 用于保存联盟的类目，综合所有平台的类目
class t_lm_cat(models.Model):
    cat_id: int = models.AutoField(primary_key=True)
    cat_mc = models.CharField(max_length=100)
    cat_bm = models.IntegerField()
    cat_jb = models.SmallIntegerField()
    cat_pre_bm = models.IntegerField()


# 用于保存各个平台上的类目信息
class t_pt_cat(models.Model):
    pt_cat_id: int = models.AutoField(primary_key=True)
    pt_cat_bm = models.IntegerField()
    pt_cat_mc = models.CharField(max_length=50)
    pt_cat_jb = models.SmallIntegerField()
    pt_pre_cat_bm = models.IntegerField()
    lm_cat = models.ForeignKey(t_lm_cat, related_name='lm_cat', on_delete=False)
    lm_pt = models.ForeignKey(t_lm_pt, related_name='lm_pt', on_delete=False)


class t_shop(models.Model):
    shop_id: int = models.AutoField(primary_key=True)
    # 商家id
    sellerid = models.CharField(max_length=100)
    # 店铺在各大平台上的id
    shop_pt_id = models.CharField(max_length=100)
    # 店铺名称
    shopname = models.CharField(max_length=300)


class t_brand(models.Model):
    brand_id: int = models.AutoField(primary_key=True)
    # 品牌code
    brandcode = models.CharField(max_length=100)
    # 品牌名
    brandname = models.CharField(max_length=300)


# 用于保存商品信息
class t_item(models.Model):
    # 商品id 自增
    sp_id: int = models.AutoField(primary_key=True)
    # 商品在平台上的id
    sp_skuId = models.CharField(max_length=100)
    # 商品名称
    sp_mc = models.CharField(max_length=300)
    # 商品url
    sp_url = models.CharField(max_length=300)
    # 商品推广url
    sp_tg_url = models.CharField(max_length=300)
    # 商品价格
    sp_jg = models.DecimalField(max_digits= 12, decimal_places=2)
    # 商品无线价格
    sp_wx_jg = models.DecimalField(max_digits= 12, decimal_places=2)
    # 商品无线推广佣金比率
    sp_wx_yjbl = models.DecimalField(max_digits= 12, decimal_places=2)
    # 商品PC推广佣金比率
    sp_pc_yjbl = models.DecimalField(max_digits= 12, decimal_places=2)
    # 商品无线推广佣金
    sp_wx_yj = models.DecimalField(max_digits= 12, decimal_places=2)
    # 商品PC推广佣金
    sp_pc_yj = models.DecimalField(max_digits= 12, decimal_places=2)
    # 商品主图url
    sp_pic_url = models.URLField()
    # 商品推广开始时间
    sp_tg_s = models.DateTimeField()
    # 商品推广结束时间
    sp_tg_e = models.DateTimeField()
    # 商品一级类目
    sp_lm_bm_1 = models.ForeignKey(t_lm_cat,on_delete=False,related_name='item_lmbm1')
    # 商品二级类目
    sp_lm_bm_2 = models.ForeignKey(t_lm_cat,on_delete=False,related_name='item_lmbm2')
    # 商品三级类目
    sp_lm_bm_3 = models.ForeignKey(t_lm_cat,on_delete=False,related_name='item_lmbm3')
    # 商品30天引单量
    sp_ydl_30 = models.IntegerField()
    # 是否爆款，1：是，0：否
    ishot = models.SmallIntegerField(default=0)
    # 商品是否为自营 0 非自营，1自营
    sp_sf_zf = models.SmallIntegerField(default=0)
    # 是否支持运费险(1:是,0:否)
    isfreefreightrisk = models.SmallIntegerField(default=0)
    # 是否包邮(1:是,0:否,2:自营商品遵从主站包邮规则)
    isfreeshipping = models.SmallIntegerField(default=0)
    # 是否秒杀(1:是,0:否)
    isseckill = models.SmallIntegerField(default=0)
    # 品牌
    brand = models.ForeignKey(t_brand, related_name='item_brand', on_delete=False)
    # 商店
    shop = models.ForeignKey(t_shop, related_name='item_shop', on_delete=False)


class t_coupon(models.Model):
    coupon_id: int = models.AutoField(primary_key=True)
    # 券种类 (优惠券种类：0 - 全品类，1 - 限品类（自营商品），2 - 限店铺，3 - 店铺限商品券)
    bindtype = models.SmallIntegerField(default=0)
    # 券面额
    discount = models.DecimalField(max_digits= 12, decimal_places=2)
    # 券链接
    link = models.URLField()
    # 商品id
    sp_item = models.ForeignKey(t_item, related_name='item_coupon', on_delete=False)


class t_images(models.Model):
    image_id: int = models.AutoField(primary_key=True)
    # 图片地址
    image_url = models.URLField()
    # 商品
    sp_item = models.ForeignKey(t_item, related_name='item_images', on_delete=False)


class t_pingou(models.Model):
    pingou_id: int = models.AutoField(primary_key=True)
    # 拼购价格
    pingouprice = models.DecimalField(max_digits= 12, decimal_places=2)
    # 拼购成团所需人数
    pingoutmcount = models.IntegerField()
    # 拼购落地页url
    pingouurl = models.URLField()
    # 拼购开始时间
    pingoustarttime = models.DateTimeField()
    # 拼购结束时间
    pingouendtime = models.DateTimeField()
    # 商品
    sp_item = models.ForeignKey(t_item, related_name='item_pingou', on_delete=False)


class t_seckill(models.Model):
    seckill_id: int = models.AutoField(primary_key=True)
    # 秒杀价原价
    seckilloriprice = models.DecimalField(max_digits= 12, decimal_places=2)
    # 秒杀价
    seckillprice = models.DecimalField(max_digits= 12, decimal_places=2)
    # 秒杀开始时间
    seckillstarttime = models.DateTimeField()
    # 秒杀结束时间
    seckillendtime = models.DateTimeField()
    # 商品
    sp_item = models.ForeignKey(t_item, related_name='item_seckill', on_delete=False)
