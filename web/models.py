from django.db import models

# Create your models here.
class t_lm_pt(models.Model):
    pt_id = models.AutoField(primary_key=True)
    pt_bm = models.IntegerField()
    pt_mc = models.CharField(max_length=20)
    pt_url = models.URLField()
    pt_created = models.DateField()


class t_lm_cat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_mc = models.CharField(max_length=100)
    cat_bm = models.IntegerField()
    cat_jb = models.SmallIntegerField()
    cat_pre_bm = models.IntegerField()

class t_pt_cat(models.Model):
    pt_cat_id = models.AutoField(primary_key=True)
    pt_cat_bm = models.IntegerField()
    pt_cat_mc = models.CharField(max_length=50)
    pt_cat_jb = models.SmallIntegerField()
    pt_pre_cat_bm = models.IntegerField()
    cat_id = models.OneToOneField(to=t_lm_cat.cat_id)
    pt_bm = models.OneToOneField(to=t_lm_pt.pt_bm)


class t_item(models.Model):
    sp_id = models.AutoField(primary_key=True)
    sp_str_id = models.CharField(100)
    sp_mc = models.CharField(max_length=300)
    sp_url = models.CharField(max_length=300)
    sp_tg_url = models.CharField(max_length=300)
    sp_jg = models.DecimalField()
    sp_pic_url = models.CharField(300)
    sp_tg_s = models.DateTimeField()
    sp_tg_e = models.DateTimeField()
    sp_lm_bm_1 = models.OneToOneField(to=t_lm_cat.cat_id)
    sp_lm_bm_2 = models.OneToOneField(to=t_lm_cat.cat_id)
    sp_lm_bm_3 = models.OneToOneField(to=t_lm_cat.cat_id)
    sp_wx_yjbl = models.DecimalField()
    sp_pc_yjbl = models.DecimalField()
    sp_ydl_30 = models.IntegerField()
    sp_sf_zf = models.SmallIntegerField(default=0) # 0 非自营，1自营