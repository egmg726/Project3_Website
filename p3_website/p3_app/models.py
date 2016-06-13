# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Brca1New(models.Model):
    gene = models.TextField(blank=True, null=True)
    varlocation = models.TextField(db_column='varLocation', blank=True, null=True)  # Field name made lowercase.
    codingeffect = models.TextField(db_column='codingEffect', blank=True, null=True)  # Field name made lowercase.
    exon = models.TextField(blank=True, null=True)
    codon = models.TextField(blank=True, null=True)
    cdna_pos = models.TextField(blank=True, null=True)
    offset = models.TextField(blank=True, null=True)
    utr3offset = models.TextField(blank=True, null=True)
    hgvs_cdna = models.TextField(blank=True, null=True)
    altname = models.TextField(blank=True, null=True)
    hgvs_prot = models.TextField(blank=True, null=True)
    hgvs_prot_code1 = models.TextField(blank=True, null=True)
    flags = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    hgmd_pubmed = models.TextField(blank=True, null=True)
    walker_pubmeds = models.TextField(blank=True, null=True)
    hgmd_pubmed_list = models.TextField(blank=True, null=True)
    google_search_new = models.TextField(blank=True, null=True)
    google_search_hits = models.TextField(blank=True, null=True)
    google_search_old = models.TextField(blank=True, null=True)
    web_search = models.TextField(blank=True, null=True)
    hg19_chr = models.TextField(blank=True, null=True)
    hg19_pos = models.TextField(blank=True, null=True)
    rsid = models.TextField(db_column='rsID', blank=True, null=True)  # Field name made lowercase.
    dbsnp_ref = models.TextField(blank=True, null=True)
    tgp_ref = models.TextField(blank=True, null=True)
    bic_count = models.TextField(blank=True, null=True)
    lovd_count = models.TextField(blank=True, null=True)
    dmudb_count = models.TextField(blank=True, null=True)
    dmudb_clasif = models.TextField(blank=True, null=True)
    hgmd_acc = models.TextField(blank=True, null=True)
    hgmd_maf = models.TextField(blank=True, null=True)
    hgmd_tag = models.TextField(blank=True, null=True)
    evs_maf_all = models.TextField(blank=True, null=True)
    evs_genotypecount_all = models.TextField(blank=True, null=True)
    evs_maf_ea = models.TextField(blank=True, null=True)
    evs_genotypecount_ea = models.TextField(blank=True, null=True)
    evs_maf_aa = models.TextField(blank=True, null=True)
    evs_genotypecount_aa = models.TextField(blank=True, null=True)
    evs_polyphen = models.TextField(blank=True, null=True)
    tgp_maf_all = models.TextField(db_column='tgp_maf_ALL', blank=True, null=True)  # Field name made lowercase.
    tgp_genotypecounts_all = models.TextField(db_column='tgp_genotypecounts_ALL', blank=True, null=True)  # Field name made lowercase.
    tgp_popsize_all = models.TextField(db_column='tgp_popsize_ALL', blank=True, null=True)  # Field name made lowercase.
    tgp_maf_eur = models.TextField(db_column='tgp_maf_EUR', blank=True, null=True)  # Field name made lowercase.
    tgp_genotypecounts_eur = models.TextField(db_column='tgp_genotypecounts_EUR', blank=True, null=True)  # Field name made lowercase.
    tgp_popsize_eur = models.TextField(db_column='tgp_popsize_EUR', blank=True, null=True)  # Field name made lowercase.
    tgp_maf_amr = models.TextField(db_column='tgp_maf_AMR', blank=True, null=True)  # Field name made lowercase.
    tgp_genotypecounts_amr = models.TextField(db_column='tgp_genotypecounts_AMR', blank=True, null=True)  # Field name made lowercase.
    tgp_popsize_amr = models.TextField(db_column='tgp_popsize_AMR', blank=True, null=True)  # Field name made lowercase.
    tgp_maf_afr = models.TextField(db_column='tgp_maf_AFR', blank=True, null=True)  # Field name made lowercase.
    tgp_genotypecounts_afr = models.TextField(db_column='tgp_genotypecounts_AFR', blank=True, null=True)  # Field name made lowercase.
    tgp_popsize_afr = models.TextField(db_column='tgp_popsize_AFR', blank=True, null=True)  # Field name made lowercase.
    tgp_maf_asn = models.TextField(db_column='tgp_maf_ASN', blank=True, null=True)  # Field name made lowercase.
    tgp_genotypecounts_asn = models.TextField(db_column='tgp_genotypecounts_ASN', blank=True, null=True)  # Field name made lowercase.
    tgp_popsize_asn = models.TextField(db_column='tgp_popsize_ASN', blank=True, null=True)  # Field name made lowercase.
    icr_count = models.TextField(blank=True, null=True)
    icr_count_hiqual = models.TextField(blank=True, null=True)
    iarc_class = models.TextField(blank=True, null=True)
    iarc_posterior_prob = models.TextField(blank=True, null=True)
    iarc_align_gvgd_priorpb = models.TextField(blank=True, null=True)
    iarc_splicing_priorpb = models.TextField(blank=True, null=True)
    iarc_combined_priorpb = models.TextField(blank=True, null=True)
    iarc_segregation_lr = models.TextField(blank=True, null=True)
    iarc_pathology_lr = models.TextField(blank=True, null=True)
    iarc_sumfamily_lr = models.TextField(blank=True, null=True)
    iarc_cooccurrence_lr = models.TextField(blank=True, null=True)
    iarc_product_of_lr = models.TextField(blank=True, null=True)
    easton_class = models.TextField(blank=True, null=True)
    easton_family_history_llr = models.TextField(blank=True, null=True)
    easton_coocurrence_llr = models.TextField(blank=True, null=True)
    easton_cosegregation_llr = models.TextField(blank=True, null=True)
    easton_combined_llr = models.TextField(blank=True, null=True)
    easton_odds_causality = models.TextField(blank=True, null=True)
    easton_odds_neutrality = models.TextField(blank=True, null=True)
    rmh_class = models.TextField(blank=True, null=True)
    lindor_odds_causality = models.TextField(blank=True, null=True)
    lindor_prior_pb_deleterious = models.TextField(blank=True, null=True)
    lindor_posterior_pb_deleterious = models.TextField(blank=True, null=True)
    houdayer_mes = models.TextField(db_column='houdayer_MES', blank=True, null=True)  # Field name made lowercase.
    houdayer_ssf = models.TextField(db_column='houdayer_SSF', blank=True, null=True)  # Field name made lowercase.
    houdayer_nnsplice = models.TextField(db_column='houdayer_NNSplice', blank=True, null=True)  # Field name made lowercase.
    houdayer_hsf = models.TextField(db_column='houdayer_HSF', blank=True, null=True)  # Field name made lowercase.
    houdayer_assa = models.TextField(db_column='houdayer_ASSA', blank=True, null=True)  # Field name made lowercase.
    houdayer_consequence = models.TextField(blank=True, null=True)
    houdayer_splice_class = models.TextField(blank=True, null=True)
    walker_methods = models.TextField(blank=True, null=True)
    walker_authors = models.TextField(blank=True, null=True)
    walker_aberrations = models.TextField(blank=True, null=True)
    walker_aberration_types = models.TextField(blank=True, null=True)
    walker_bioinf_preds = models.TextField(blank=True, null=True)
    walker_func_assays = models.TextField(blank=True, null=True)
    alamut_agvgdclass = models.TextField(db_column='alamut_AGVGDclass', blank=True, null=True)  # Field name made lowercase.
    alamut_agvgdgv = models.TextField(db_column='alamut_AGVGDgv', blank=True, null=True)  # Field name made lowercase.
    alamut_agvgdgd = models.TextField(db_column='alamut_AGVGDgd', blank=True, null=True)  # Field name made lowercase.
    swissprot_type = models.TextField(blank=True, null=True)
    swissprot_range = models.TextField(blank=True, null=True)
    swissprot_desc = models.TextField(blank=True, null=True)
    alamut_proteindomain1 = models.TextField(db_column='alamut_proteinDomain1', blank=True, null=True)  # Field name made lowercase.
    alamut_proteindomain2 = models.TextField(db_column='alamut_proteinDomain2', blank=True, null=True)  # Field name made lowercase.
    alamut_proteindomain3 = models.TextField(db_column='alamut_proteinDomain3', blank=True, null=True)  # Field name made lowercase.
    alamut_proteindomain4 = models.TextField(db_column='alamut_proteinDomain4', blank=True, null=True)  # Field name made lowercase.
    alamut_siftprediction = models.TextField(db_column='alamut_SIFTprediction', blank=True, null=True)  # Field name made lowercase.
    alamut_siftweight = models.TextField(db_column='alamut_SIFTweight', blank=True, null=True)  # Field name made lowercase.
    alamut_siftmedian = models.TextField(db_column='alamut_SIFTmedian', blank=True, null=True)  # Field name made lowercase.
    alamut_mappprediction = models.TextField(db_column='alamut_MAPPprediction', blank=True, null=True)  # Field name made lowercase.
    alamut_mapppvalue = models.TextField(db_column='alamut_MAPPpValue', blank=True, null=True)  # Field name made lowercase.
    alamut_mapppvaluemedian = models.TextField(db_column='alamut_MAPPpValueMedian', blank=True, null=True)  # Field name made lowercase.
    alamut_conservedorthos = models.TextField(db_column='alamut_conservedOrthos', blank=True, null=True)  # Field name made lowercase.
    alamut_conserveddistspecies = models.TextField(db_column='alamut_conservedDistSpecies', blank=True, null=True)  # Field name made lowercase.
    alamut_blosum45 = models.TextField(db_column='alamut_BLOSUM45', blank=True, null=True)  # Field name made lowercase.
    alamut_blosum62 = models.TextField(db_column='alamut_BLOSUM62', blank=True, null=True)  # Field name made lowercase.
    alamut_blosum80 = models.TextField(db_column='alamut_BLOSUM80', blank=True, null=True)  # Field name made lowercase.
    alamut_distnearestss = models.TextField(db_column='alamut_distNearestSS', blank=True, null=True)  # Field name made lowercase.
    alamut_nearestsstype = models.TextField(db_column='alamut_nearestSSType', blank=True, null=True)  # Field name made lowercase.
    alamut_nearestsschange = models.TextField(db_column='alamut_nearestSSChange', blank=True, null=True)  # Field name made lowercase.
    firstorlast3 = models.TextField(blank=True, null=True)
    alamut_wtssfscore = models.TextField(db_column='alamut_wtSSFScore', blank=True, null=True)  # Field name made lowercase.
    alamut_varssfscore = models.TextField(db_column='alamut_varSSFScore', blank=True, null=True)  # Field name made lowercase.
    alamut_changessfscore = models.TextField(db_column='alamut_changeSSFScore', blank=True, null=True)  # Field name made lowercase.
    alamut_wtmaxentscore = models.TextField(db_column='alamut_wtMaxEntScore', blank=True, null=True)  # Field name made lowercase.
    alamut_varmaxentscore = models.TextField(db_column='alamut_varMaxEntScore', blank=True, null=True)  # Field name made lowercase.
    alamut_changemaxentscore = models.TextField(db_column='alamut_changeMaxEntScore', blank=True, null=True)  # Field name made lowercase.
    alamut_wtnnsscore = models.TextField(db_column='alamut_wtNNSScore', blank=True, null=True)  # Field name made lowercase.
    alamut_varnnsscore = models.TextField(db_column='alamut_varNNSScore', blank=True, null=True)  # Field name made lowercase.
    alamut_changennsscore = models.TextField(db_column='alamut_changeNNSScore', blank=True, null=True)  # Field name made lowercase.
    alamut_wtgsscore = models.TextField(db_column='alamut_wtGSScore', blank=True, null=True)  # Field name made lowercase.
    alamut_vargsscore = models.TextField(db_column='alamut_varGSScore', blank=True, null=True)  # Field name made lowercase.
    alamut_changegsscore = models.TextField(db_column='alamut_changeGSScore', blank=True, null=True)  # Field name made lowercase.
    alamut_wthsfscore = models.TextField(db_column='alamut_wtHSFScore', blank=True, null=True)  # Field name made lowercase.
    alamut_varhsfscore = models.TextField(db_column='alamut_varHSFScore', blank=True, null=True)  # Field name made lowercase.
    alamut_changehsfscore = models.TextField(db_column='alamut_changeHSFScore', blank=True, null=True)  # Field name made lowercase.
    alamut_localspliceeffect = models.TextField(db_column='alamut_localSpliceEffect', blank=True, null=True)  # Field name made lowercase.
    muttaster_model = models.TextField(blank=True, null=True)
    muttaster_prediction = models.TextField(blank=True, null=True)
    muttaster_p_pred = models.TextField(blank=True, null=True)
    muttaster_features = models.TextField(blank=True, null=True)
    polyphen2_prediction = models.TextField(blank=True, null=True)
    polyphen2_based_on = models.TextField(blank=True, null=True)
    polyphen2_effect = models.TextField(blank=True, null=True)
    polyphen2_site = models.TextField(blank=True, null=True)
    polyphen2_region = models.TextField(blank=True, null=True)
    polyphen2_hdiv_prediction = models.TextField(blank=True, null=True)
    polyphen2_hdiv_class = models.TextField(blank=True, null=True)
    polyphen2_hdiv_prob = models.TextField(blank=True, null=True)
    polyphen2_hdiv_fpr = models.TextField(blank=True, null=True)
    polyphen2_hdiv_tpr = models.TextField(blank=True, null=True)
    polyphen2_hdiv_fdr = models.TextField(blank=True, null=True)
    polyphen2_hvar_prediction = models.TextField(blank=True, null=True)
    polyphen2_hvar_class = models.TextField(blank=True, null=True)
    polyphen2_hvar_prob = models.TextField(blank=True, null=True)
    polyphen2_hvar_fpr = models.TextField(blank=True, null=True)
    polyphen2_hvar_tpr = models.TextField(blank=True, null=True)
    polyphen2_hvar_fdr = models.TextField(blank=True, null=True)
    bouwman_mutation_type = models.TextField(blank=True, null=True)
    bouwman_aligngvgd = models.TextField(db_column='bouwman_AlignGVGD', blank=True, null=True)  # Field name made lowercase.
    bouwman_predicted_splice_effect = models.TextField(blank=True, null=True)
    bouwman_lit_predictions = models.TextField(blank=True, null=True)
    bouwman_growth = models.TextField(blank=True, null=True)
    bouwman_ic50 = models.TextField(db_column='bouwman_IC50', blank=True, null=True)  # Field name made lowercase.
    bouwman_classification = models.TextField(blank=True, null=True)
    umd_significance = models.TextField(blank=True, null=True)
    umd_count = models.TextField(blank=True, null=True)
    cadd_rawscore = models.TextField(db_column='cadd_RawScore', blank=True, null=True)  # Field name made lowercase.
    cadd_cscore = models.TextField(db_column='cadd_Cscore', blank=True, null=True)  # Field name made lowercase.
    suspect_score = models.TextField(blank=True, null=True)
    id = models.IntegerField(blank=True,primary_key=True)

    class Meta:
        managed = False
        db_table = 'brca1_new'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
