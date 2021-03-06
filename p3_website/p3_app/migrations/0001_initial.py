# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-13 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brca1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene', models.TextField(blank=True, null=True)),
                ('varlocation', models.TextField(blank=True, db_column='varLocation', null=True)),
                ('codingeffect', models.TextField(blank=True, db_column='codingEffect', null=True)),
                ('exon', models.TextField(blank=True, null=True)),
                ('codon', models.TextField(blank=True, null=True)),
                ('cdna_pos', models.TextField(blank=True, null=True)),
                ('offset', models.TextField(blank=True, null=True)),
                ('utr3offset', models.TextField(blank=True, null=True)),
                ('hgvs_cdna', models.TextField(blank=True, null=True)),
                ('altname', models.TextField(blank=True, null=True)),
                ('hgvs_prot', models.TextField(blank=True, null=True)),
                ('hgvs_prot_code1', models.TextField(blank=True, null=True)),
                ('flags', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('hgmd_pubmed', models.TextField(blank=True, null=True)),
                ('walker_pubmeds', models.TextField(blank=True, null=True)),
                ('hgmd_pubmed_list', models.TextField(blank=True, null=True)),
                ('google_search_new', models.TextField(blank=True, null=True)),
                ('google_search_hits', models.TextField(blank=True, null=True)),
                ('google_search_old', models.TextField(blank=True, null=True)),
                ('web_search', models.TextField(blank=True, null=True)),
                ('hg19_chr', models.TextField(blank=True, null=True)),
                ('hg19_pos', models.TextField(blank=True, null=True)),
                ('rsid', models.TextField(blank=True, db_column='rsID', null=True)),
                ('dbsnp_ref', models.TextField(blank=True, null=True)),
                ('tgp_ref', models.TextField(blank=True, null=True)),
                ('bic_count', models.TextField(blank=True, null=True)),
                ('lovd_count', models.TextField(blank=True, null=True)),
                ('dmudb_count', models.TextField(blank=True, null=True)),
                ('dmudb_clasif', models.TextField(blank=True, null=True)),
                ('hgmd_acc', models.TextField(blank=True, null=True)),
                ('hgmd_maf', models.TextField(blank=True, null=True)),
                ('hgmd_tag', models.TextField(blank=True, null=True)),
                ('evs_maf_all', models.TextField(blank=True, null=True)),
                ('evs_genotypecount_all', models.TextField(blank=True, null=True)),
                ('evs_maf_ea', models.TextField(blank=True, null=True)),
                ('evs_genotypecount_ea', models.TextField(blank=True, null=True)),
                ('evs_maf_aa', models.TextField(blank=True, null=True)),
                ('evs_genotypecount_aa', models.TextField(blank=True, null=True)),
                ('evs_polyphen', models.TextField(blank=True, null=True)),
                ('tgp_maf_all', models.TextField(blank=True, db_column='tgp_maf_ALL', null=True)),
                ('tgp_genotypecounts_all', models.TextField(blank=True, db_column='tgp_genotypecounts_ALL', null=True)),
                ('tgp_popsize_all', models.TextField(blank=True, db_column='tgp_popsize_ALL', null=True)),
                ('tgp_maf_eur', models.TextField(blank=True, db_column='tgp_maf_EUR', null=True)),
                ('tgp_genotypecounts_eur', models.TextField(blank=True, db_column='tgp_genotypecounts_EUR', null=True)),
                ('tgp_popsize_eur', models.TextField(blank=True, db_column='tgp_popsize_EUR', null=True)),
                ('tgp_maf_amr', models.TextField(blank=True, db_column='tgp_maf_AMR', null=True)),
                ('tgp_genotypecounts_amr', models.TextField(blank=True, db_column='tgp_genotypecounts_AMR', null=True)),
                ('tgp_popsize_amr', models.TextField(blank=True, db_column='tgp_popsize_AMR', null=True)),
                ('tgp_maf_afr', models.TextField(blank=True, db_column='tgp_maf_AFR', null=True)),
                ('tgp_genotypecounts_afr', models.TextField(blank=True, db_column='tgp_genotypecounts_AFR', null=True)),
                ('tgp_popsize_afr', models.TextField(blank=True, db_column='tgp_popsize_AFR', null=True)),
                ('tgp_maf_asn', models.TextField(blank=True, db_column='tgp_maf_ASN', null=True)),
                ('tgp_genotypecounts_asn', models.TextField(blank=True, db_column='tgp_genotypecounts_ASN', null=True)),
                ('tgp_popsize_asn', models.TextField(blank=True, db_column='tgp_popsize_ASN', null=True)),
                ('icr_count', models.TextField(blank=True, null=True)),
                ('icr_count_hiqual', models.TextField(blank=True, null=True)),
                ('iarc_class', models.TextField(blank=True, null=True)),
                ('iarc_posterior_prob', models.TextField(blank=True, null=True)),
                ('iarc_align_gvgd_priorpb', models.TextField(blank=True, null=True)),
                ('iarc_splicing_priorpb', models.TextField(blank=True, null=True)),
                ('iarc_combined_priorpb', models.TextField(blank=True, null=True)),
                ('iarc_segregation_lr', models.TextField(blank=True, null=True)),
                ('iarc_pathology_lr', models.TextField(blank=True, null=True)),
                ('iarc_sumfamily_lr', models.TextField(blank=True, null=True)),
                ('iarc_cooccurrence_lr', models.TextField(blank=True, null=True)),
                ('iarc_product_of_lr', models.TextField(blank=True, null=True)),
                ('easton_class', models.TextField(blank=True, null=True)),
                ('easton_family_history_llr', models.TextField(blank=True, null=True)),
                ('easton_coocurrence_llr', models.TextField(blank=True, null=True)),
                ('easton_cosegregation_llr', models.TextField(blank=True, null=True)),
                ('easton_combined_llr', models.TextField(blank=True, null=True)),
                ('easton_odds_causality', models.TextField(blank=True, null=True)),
                ('easton_odds_neutrality', models.TextField(blank=True, null=True)),
                ('rmh_class', models.TextField(blank=True, null=True)),
                ('lindor_odds_causality', models.TextField(blank=True, null=True)),
                ('lindor_prior_pb_deleterious', models.TextField(blank=True, null=True)),
                ('lindor_posterior_pb_deleterious', models.TextField(blank=True, null=True)),
                ('houdayer_mes', models.TextField(blank=True, db_column='houdayer_MES', null=True)),
                ('houdayer_ssf', models.TextField(blank=True, db_column='houdayer_SSF', null=True)),
                ('houdayer_nnsplice', models.TextField(blank=True, db_column='houdayer_NNSplice', null=True)),
                ('houdayer_hsf', models.TextField(blank=True, db_column='houdayer_HSF', null=True)),
                ('houdayer_assa', models.TextField(blank=True, db_column='houdayer_ASSA', null=True)),
                ('houdayer_consequence', models.TextField(blank=True, null=True)),
                ('houdayer_splice_class', models.TextField(blank=True, null=True)),
                ('walker_methods', models.TextField(blank=True, null=True)),
                ('walker_authors', models.TextField(blank=True, null=True)),
                ('walker_aberrations', models.TextField(blank=True, null=True)),
                ('walker_aberration_types', models.TextField(blank=True, null=True)),
                ('walker_bioinf_preds', models.TextField(blank=True, null=True)),
                ('walker_func_assays', models.TextField(blank=True, null=True)),
                ('alamut_agvgdclass', models.TextField(blank=True, db_column='alamut_AGVGDclass', null=True)),
                ('alamut_agvgdgv', models.TextField(blank=True, db_column='alamut_AGVGDgv', null=True)),
                ('alamut_agvgdgd', models.TextField(blank=True, db_column='alamut_AGVGDgd', null=True)),
                ('swissprot_type', models.TextField(blank=True, null=True)),
                ('swissprot_range', models.TextField(blank=True, null=True)),
                ('swissprot_desc', models.TextField(blank=True, null=True)),
                ('alamut_proteindomain1', models.TextField(blank=True, db_column='alamut_proteinDomain1', null=True)),
                ('alamut_proteindomain2', models.TextField(blank=True, db_column='alamut_proteinDomain2', null=True)),
                ('alamut_proteindomain3', models.TextField(blank=True, db_column='alamut_proteinDomain3', null=True)),
                ('alamut_proteindomain4', models.TextField(blank=True, db_column='alamut_proteinDomain4', null=True)),
                ('alamut_siftprediction', models.TextField(blank=True, db_column='alamut_SIFTprediction', null=True)),
                ('alamut_siftweight', models.TextField(blank=True, db_column='alamut_SIFTweight', null=True)),
                ('alamut_siftmedian', models.TextField(blank=True, db_column='alamut_SIFTmedian', null=True)),
                ('alamut_mappprediction', models.TextField(blank=True, db_column='alamut_MAPPprediction', null=True)),
                ('alamut_mapppvalue', models.TextField(blank=True, db_column='alamut_MAPPpValue', null=True)),
                ('alamut_mapppvaluemedian', models.TextField(blank=True, db_column='alamut_MAPPpValueMedian', null=True)),
                ('alamut_conservedorthos', models.TextField(blank=True, db_column='alamut_conservedOrthos', null=True)),
                ('alamut_conserveddistspecies', models.TextField(blank=True, db_column='alamut_conservedDistSpecies', null=True)),
                ('alamut_blosum45', models.TextField(blank=True, db_column='alamut_BLOSUM45', null=True)),
                ('alamut_blosum62', models.TextField(blank=True, db_column='alamut_BLOSUM62', null=True)),
                ('alamut_blosum80', models.TextField(blank=True, db_column='alamut_BLOSUM80', null=True)),
                ('alamut_distnearestss', models.TextField(blank=True, db_column='alamut_distNearestSS', null=True)),
                ('alamut_nearestsstype', models.TextField(blank=True, db_column='alamut_nearestSSType', null=True)),
                ('alamut_nearestsschange', models.TextField(blank=True, db_column='alamut_nearestSSChange', null=True)),
                ('firstorlast3', models.TextField(blank=True, null=True)),
                ('alamut_wtssfscore', models.TextField(blank=True, db_column='alamut_wtSSFScore', null=True)),
                ('alamut_varssfscore', models.TextField(blank=True, db_column='alamut_varSSFScore', null=True)),
                ('alamut_changessfscore', models.TextField(blank=True, db_column='alamut_changeSSFScore', null=True)),
                ('alamut_wtmaxentscore', models.TextField(blank=True, db_column='alamut_wtMaxEntScore', null=True)),
                ('alamut_varmaxentscore', models.TextField(blank=True, db_column='alamut_varMaxEntScore', null=True)),
                ('alamut_changemaxentscore', models.TextField(blank=True, db_column='alamut_changeMaxEntScore', null=True)),
                ('alamut_wtnnsscore', models.TextField(blank=True, db_column='alamut_wtNNSScore', null=True)),
                ('alamut_varnnsscore', models.TextField(blank=True, db_column='alamut_varNNSScore', null=True)),
                ('alamut_changennsscore', models.TextField(blank=True, db_column='alamut_changeNNSScore', null=True)),
                ('alamut_wtgsscore', models.TextField(blank=True, db_column='alamut_wtGSScore', null=True)),
                ('alamut_vargsscore', models.TextField(blank=True, db_column='alamut_varGSScore', null=True)),
                ('alamut_changegsscore', models.TextField(blank=True, db_column='alamut_changeGSScore', null=True)),
                ('alamut_wthsfscore', models.TextField(blank=True, db_column='alamut_wtHSFScore', null=True)),
                ('alamut_varhsfscore', models.TextField(blank=True, db_column='alamut_varHSFScore', null=True)),
                ('alamut_changehsfscore', models.TextField(blank=True, db_column='alamut_changeHSFScore', null=True)),
                ('alamut_localspliceeffect', models.TextField(blank=True, db_column='alamut_localSpliceEffect', null=True)),
                ('muttaster_model', models.TextField(blank=True, null=True)),
                ('muttaster_prediction', models.TextField(blank=True, null=True)),
                ('muttaster_p_pred', models.TextField(blank=True, null=True)),
                ('muttaster_features', models.TextField(blank=True, null=True)),
                ('polyphen2_prediction', models.TextField(blank=True, null=True)),
                ('polyphen2_based_on', models.TextField(blank=True, null=True)),
                ('polyphen2_effect', models.TextField(blank=True, null=True)),
                ('polyphen2_site', models.TextField(blank=True, null=True)),
                ('polyphen2_region', models.TextField(blank=True, null=True)),
                ('polyphen2_hdiv_prediction', models.TextField(blank=True, null=True)),
                ('polyphen2_hdiv_class', models.TextField(blank=True, null=True)),
                ('polyphen2_hdiv_prob', models.TextField(blank=True, null=True)),
                ('polyphen2_hdiv_fpr', models.TextField(blank=True, null=True)),
                ('polyphen2_hdiv_tpr', models.TextField(blank=True, null=True)),
                ('polyphen2_hdiv_fdr', models.TextField(blank=True, null=True)),
                ('polyphen2_hvar_prediction', models.TextField(blank=True, null=True)),
                ('polyphen2_hvar_class', models.TextField(blank=True, null=True)),
                ('polyphen2_hvar_prob', models.TextField(blank=True, null=True)),
                ('polyphen2_hvar_fpr', models.TextField(blank=True, null=True)),
                ('polyphen2_hvar_tpr', models.TextField(blank=True, null=True)),
                ('polyphen2_hvar_fdr', models.TextField(blank=True, null=True)),
                ('bouwman_mutation_type', models.TextField(blank=True, null=True)),
                ('bouwman_aligngvgd', models.TextField(blank=True, db_column='bouwman_AlignGVGD', null=True)),
                ('bouwman_predicted_splice_effect', models.TextField(blank=True, null=True)),
                ('bouwman_lit_predictions', models.TextField(blank=True, null=True)),
                ('bouwman_growth', models.TextField(blank=True, null=True)),
                ('bouwman_ic50', models.TextField(blank=True, db_column='bouwman_IC50', null=True)),
                ('bouwman_classification', models.TextField(blank=True, null=True)),
                ('umd_significance', models.TextField(blank=True, null=True)),
                ('umd_count', models.TextField(blank=True, null=True)),
                ('cadd_rawscore', models.TextField(blank=True, db_column='cadd_RawScore', null=True)),
                ('cadd_cscore', models.TextField(blank=True, db_column='cadd_Cscore', null=True)),
                ('suspect_score', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'brca1_new',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
    ]
