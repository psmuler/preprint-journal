# root scopus directory
root = "/disks/qnap3/shared/scopus-24/data/"
# openalex_dir = "/disks/qnap3/users/23-miura/openalex-snapshot/processed_json/"
openalex_dir = "s3://openalex-bulk/"

"""c-miura@ti01:/disks/qnap3/users/23-miura/openalex-snapshot/processed_json/works$ ls
abstract.jsonl.gz                        best_oa_location_is_oa.jsonl.gz             concepts.jsonl.gz                       grants.jsonl.gz                       mesh.jsonl.gz                               referenced_works_count.jsonl.gz         topics_id.jsonl.gz
apc_list.jsonl.gz                        best_oa_location_landing_page_url.jsonl.gz  corresponding_author_ids.jsonl.gz       has_fulltext.jsonl.gz                 open_access.jsonl.gz                        referenced_works.jsonl.gz               topics.jsonl.gz
apc_paid.jsonl.gz                        best_oa_location_license.jsonl.gz           corresponding_institution_ids.jsonl.gz  ids.jsonl.gz                          primary_location_id.jsonl.gz                referenced_works.parquet.zstd           topics_score.jsonl.gz
author_countries.jsonl.gz                best_oa_location_pdf_url.jsonl.gz           countries_distinct_count.jsonl.gz       indexed_in.jsonl.gz                   primary_location_is_oa.jsonl.gz             referenced_works_valid.jsonl.gz         type_crossref.jsonl.gz
author_id.jsonl.gz                       best_oa_location_version.jsonl.gz           counts_by_year.jsonl.gz                 institution_assertions.jsonl.gz       primary_location_landing_page_url.jsonl.gz  reference.parquet                       type_id.jsonl.gz
author_institutions.jsonl.gz             biblio.jsonl.gz                             created_date.jsonl.gz                   institutions_distinct_count.jsonl.gz  primary_location_license.jsonl.gz           reference.parquet.zstd                  type.jsonl.gz
author_is_corresponding.jsonl.gz         citation_normalized_percentile.jsonl.gz     datasets.jsonl.gz                       is_paratext.jsonl.gz                  primary_location_pdf_url.jsonl.gz           related_works.jsonl.gz                  updated_date.jsonl.gz
author_position.jsonl.gz                 cited_by_count.jsonl.gz                     display_name.jsonl.gz                   is_retracted.jsonl.gz                 primary_location_version.jsonl.gz           summary_stats.jsonl.gz                  versions.jsonl.gz
author_raw_affiliation_strings.jsonl.gz  cited_by.jsonl.gz                           doi.jsonl.gz                            keywords.jsonl.gz                     primary_topic_id.jsonl.gz                   sustainable_development_goals.jsonl.gz
authors_count.jsonl.gz                   cited_by.parquet.zstd                       doi_registration_agency.jsonl.gz        language_id.jsonl.gz                  primary_topic.jsonl.gz                      title.jsonl.gz
authorships_truncated.jsonl.gz           cited_by_percentile_year.jsonl.gz           fulltext_origin.jsonl.gz                language.jsonl.gz                     publication_date.jsonl.gz                   topic_field_subfield_table.tsv
best_oa_location_id.jsonl.gz             concepts_count.jsonl.gz                     fwci.jsonl.gz                           locations_count.jsonl.gz              publication_year.jsonl.gz                   topics_count.jsonl.gz
"""

"""
c-miura@ti04:/disks/qnap3/users/23-miura/openalex-snapshot/processed/sources$ ls
abbreviated_title-000.gz  display_name-000.gz                     ids.issn-000.gz              issn_l-000.gz                            summary_stats.2yr_mean_citedness-000.gz  type-000.gz
alternate_titles-000.gz   homepage_url-000.gz                     ids.issn_l-000.gz            publisher-000.gz                         summary_stats.2yr_works_count-000.gz     type_id-000.gz
apc_prices-000.gz         host_institution_lineage-000.gz         ids.mag-000.gz               publisher_id-000.gz                      summary_stats.cited_by_count-000.gz      updated_date-000.gz
apc_usd-000.gz            host_institution_lineage_names-000.gz   ids.wikidata-000.gz          publisher_lineage-000.gz                 summary_stats.h_index-000.gz             works_count-000.gz
cited_by_count-000.gz     host_organization-000.gz                is_core-000.gz               publisher_lineage_names-000.gz           summary_stats.i10_index-000.gz           x_concepts-000.gz
country_code-000.gz       host_organization_lineage-000.gz        is_indexed_in_scopus-000.gz  societies-000.gz                         summary_stats.oa_percent-000.gz
country_id-000.gz         host_organization_lineage_names-000.gz  is_in_doaj-000.gz            summary_stats.2yr_cited_by_count-000.gz  summary_stats.works_count-000.gz
counts_by_year-000.gz     host_organization_name-000.gz           is_oa-000.gz                 summary_stats.2yr_h_index-000.gz         topics-000.gz
created_date-000.gz       ids.fatcat-000.gz                       issn-000.gz                  summary_stats.2yr_i10_index-000.gz       topic_share-000.gz
"""

major_journal_ids = [
    19700182758,
    10600153309,
    21100200805,
    21121,
    4000151810,
    17945,
    21100201068,
    14204,
    17495,
    4000151808,
    28222,
    21100457028,
    21100907125,
    19700188403,
    4000151809,
    21100924827,
    40944,
    14859,
    15537,
    17592,
    12216,
    22214,
    17929,
    22173,
    12977,
    14531,
    21206,
    21727,
    20250,
    21100229161,
    21100226442,
    14855,
    21100782808,
    21100778827,
    25879,
    18556,
    23571,
    18434,
    21100239256,
    19700182013,
    20297,
    21100850723,
    # Proceedings of the Royal Society B: Biological Sciences, not found
    18606,
    17978,
    11900154404,
    18555,
    18605,
    19908,
    21100850718,
]

fetched_topics_list = [
	"T10015",  "T10521", "T11339",
	"T10044",  "T10602", "T11385",
	"T10066",  "T10604", "T11482",
	"T10123",  "T10621", "T11559",
	"T10207",  "T10691", "T11561",
	"T10222",  "T10725", "T11663",
	"T10240",  "T10773", "T11710",
	"T10269",  "T10836", "T11786",
	"T10301",  "T10878", "T11882",
	"T10303",  "T10885", "T11927",
	"T10404",   "T11956",
	"T10407",  "T10911", "T11970",
	"T10422",  "T10932", "T12388",
	"T10432",  "T11041", "T12561",
	"T10441",  "T11072", "T12827",
	"T10493",  "T11075", "T13937",
	"T10497",  "T11178", "T14285",
	"T10505",
	# 2025/3/4
	'T11924', 'T12140', 'T10887', 'T10294', 'T11919', 'T11515', 'T11219', 'T11533', 'T11078', 'T13157', 'T12412', 'T10169', 'T12254', 'T12009', 'T12620', 'T12763', 'T12187', 'T10268', 'T11841', 'T10929', 'T11765', 'T11308', 'T12215', 'T12668', 'T11889', 'T12534', 'T12756', 'T11237', 'T12688', 'T12566', 'T13221', 'T13047', 'T13725', 'T13651', 'T12434', 'T12683', 'T12946', 'T14065', 'T12360', 'T13223', 'T12789', 'T13437', 'T13188', 'T11124', 'T12029', 'T10952', 'T13526', 'T14049', 'T11818', 'T11908', 'T11845', 'T11879', 'T10724', 'T12820', 'T13426', 'T11305', 'T12104', 'T12867', 'T12030', 'T11335', 'T11501', 'T11289', 'T11848', 'T12685', 'T13454', 'T11677', 'T11884', 'T12610', 'T10934', 'T12441', 'T11480', 'T12287', 'T12576', 'T13736', 'T13326', 'T13012', 'T11736', 'T11332', 'T12257', 'T10593', 'T12835', 'T12530', 'T13187', 'T14135'
]

columns_must_fetch = [
    "id",
    "counts_by_year",
    "publication_year",
    "publication_date",
    "authorships",
    "primary_topic",
    "cited_by_count",
    "doi",
    "locations",
    "locations_count",
    "referenced_works",
    "referenced_works_count",
]

ai_related = [
    "cs.AI",  # Artificial Intelligence
    "cs.CL",  # Computation and Language
    "cs.CV",  # Computer Vision and Pattern Recognition
    "cs.LG",  # Machine Learning
    "cs.MA",  # Multiagent Systems
    "cs.NE",  # Neural and Evolutionary Computing
    "cs.RO",  # Robotics
    "cs.SI",  # Social and Information Networks
]
others = [
    "cs.AR",  # Hardware Architecture
    "cs.CC",  # Computational Complexity
    "cs.CE",  # Computational Engineering, Finance, and Science
    "cs.CG",  # Computational Geometry
    "cs.CR",  # Cryptography and Security
    "cs.CY",  # Computers and Society
    "cs.DB",  # Databases
    "cs.DC",  # Distributed, Parallel, and Cluster Computing
    "cs.DL",  # Digital Libraries
    "cs.DM",  # Discrete Mathematics
    "cs.DS",  # Data Structures and Algorithms
    "cs.ET",  # Emerging Technologies
    "cs.FL",  # Formal Languages and Automata Theory
    "cs.GL",  # General Literature
    "cs.GR",  # Graphics
    "cs.GT",  # Computer Science and Game Theory
    "cs.HC",  # Human-Computer Interaction
    "cs.IR",  # Information Retrieval
    "cs.IT",  # Information Theory
    "cs.LO",  # Logic in Computer Science
    "cs.MM",  # Multimedia
    "cs.MS",  # Mathematical Software
    "cs.NA",  # Numerical Analysis
    "cs.NI",  # Networking and Internet Architecture
    "cs.OH",  # Other Computer Science
    "cs.OS",  # Operating Systems
    "cs.PF",  # Performance
    "cs.PL",  # Programming Languages
    "cs.SC",  # Symbolic Computation
    "cs.SD",  # Sound
    "cs.SE",  # Software Engineering
    "cs.SY",  # Systems and Control
]

mapping = {
    **{cat: f"cs_ai.{cat.split('.')[-1]}" for cat in ai_related},
    **{cat: f"cs_other.{cat.split('.')[-1]}" for cat in others}
}
arxiv_category_to_subfield ={
    "astro-ph.CO":"astro-ph",
    "astro-ph.EP":"astro-ph",
    "astro-ph.GA":"astro-ph",
    "astro-ph.HE":"astro-ph",
    "astro-ph.IM":"astro-ph",
    "astro-ph.SR":"astro-ph",
    "cs.CG":"cs",
    "cs.CL":"cs",
    "cs.CR":"cs",
    "cs.CV":"cs",
    "cs.CY":"cs",
    "cs.DB":"cs",
    "cs.DC":"cs",
    "cs.DL":"cs",
    "cs.DM":"cs",
    "cs.DS":"cs",
    "cs.ET":"cs",
    "cs.FL":"cs",
    "cs.GL":"cs",
    "cs.GR":"cs",
    "cs.GT":"cs",
    "cs.HC":"cs",
    "cs.IR":"cs",
    "cs.IT":"cs",
    "cs.LG":"cs",
    "cs.LO":"cs",
    "cs.MA":"cs",
    "cs.MM":"cs",
    "cs.MS":"cs",
    "cs.NA":"cs",
    "cs.NE":"cs",
    "cs.NI":"cs",
    "cs.OH":"cs",
    "cs.OS":"cs",
    "cs.PF":"cs",
    "cs.PL":"cs",
    "cs.RO":"cs",
    "cs.SC":"cs",
    "cs.SD":"cs",
    "cs.SE":"cs",
    "cs.SI":"cs",
    "cs.SY":"cs",
    "econ.EM":"econ",
    "econ.GN":"econ",
    "econ.TH":"econ",
    "eess.AS":"eess",
    "eess.IV":"eess",
    "eess.SP":"eess",
    "eess.SY":"eess",
    "math.AC":"math",
    "math.AG":"math",
    "math.AP":"math",
    "math.AT":"math",
    "math.CA":"math",
    "math.CO":"math",
    "math.CT":"math",
    "math.CV":"math",
    "math.DG":"math",
    "math.DS":"math",
    "math.FA":"math",
    "math.GM":"math",
    "math.GN":"math",
    "math.GR":"math",
    "math.GT":"math",
    "math.HO":"math",
    "math.IT":"math",
    "math.KT":"math",
    "math.LO":"math",
    "math.MG":"math",
    "math.MP":"math",
    "math.NA":"math",
    "math.NT":"math",
    "math.OA":"math",
    "math.OC":"math",
    "math.PR":"math",
    "math.QA":"math",
    "math.RA":"math",
    "math.RT":"math",
    "math.SG":"math",
    "math.SP":"math",
    "math.ST":"math",
    "q-bio.BM":"q-bio",
    "q-bio.CB":"q-bio",
    "q-bio.GN":"q-bio",
    "q-bio.MN":"q-bio",
    "q-bio.NC":"q-bio",
    "q-bio.OT":"q-bio",
    "q-bio.PE":"q-bio",
    "q-bio.QM":"q-bio",
    "q-bio.SC":"q-bio",
    "q-bio.TO":"q-bio",
    "q-fin.CP":"q-fin",
    "q-fin.EC":"q-fin",
    "q-fin.GN":"q-fin",
    "q-fin.MF":"q-fin",
    "q-fin.PM":"q-fin",
    "q-fin.PR":"q-fin",
    "q-fin.RM":"q-fin",
    "q-fin.ST":"q-fin",
    "q-fin.TR":"q-fin",
    "stat.AP":"stat",
    "stat.CO":"stat",
    "stat.ME":"stat",
    "stat.ML":"stat",
    "stat.OT":"stat",
    "stat.TH":"stat",
    "cond-mat.dis-nn":"cond-mat",
    "cond-mat.mes-hall":"cond-mat",
    "cond-mat.mtrl-sci":"cond-mat",
    "cond-mat.other":"cond-mat",
    "cond-mat.quant-gas":"cond-mat",
    "cond-mat.soft":"cond-mat",
    "cond-mat.stat-mech":"cond-mat",
    "cond-mat.str-el":"cond-mat",
    "cond-mat.supr-con":"cond-mat",
    "hep-ex":"hep",
    "hep-lat":"hep",
    "hep-ph":"hep",
    "hep-th":"hep",
    "nlin.AO":"nlin",
    "nlin.CD":"nlin",
    "nlin.CG":"nlin",
    "nlin.PS":"nlin",
    "nlin.SI":"nlin",
    "nucl-ex":"nucl",
    "nucl-th":"nucl",
    "physics.acc-ph":"physics",
    "physics.ao-ph":"physics",
    "physics.app-ph":"physics",
    "physics.atm-clus":"physics",
    "physics.atom-ph":"physics",
    "physics.bio-ph":"physics",
    "physics.chem-ph":"physics",
    "physics.class-ph":"physics",
    "physics.comp-ph":"physics",
    "physics.data-an":"physics",
    "physics.ed-ph":"physics",
    "physics.flu-dyn":"physics",
    "physics.gen-ph":"physics",
    "physics.geo-ph":"physics",
    "physics.hist-ph":"physics",
    "physics.ins-det":"physics",
    "physics.med-ph":"physics",
    "physics.optics":"physics",
    "physics.plasm-ph":"physics",
    "physics.pop-ph":"physics",
    "physics.soc-ph":"physics",
    "physics.space-ph":"physics",
}

category_to_subfield = { # updated on 2025/05/15
    "animal-behavior-and-cognition":"behav",
    "developmental-biology":"behav",
    "neuroscience":"behav",
    "zoology":"behav",

    "cancer-biology":"biomed",
    "clinical-trials":"biomed",
    "epidemiology":"biomed",
    "immunology":"biomed",
    "pathology":"biomed",
    "pharmacology-and-toxicology":"biomed",
    "physiology":"biomed",

    "ecology":"evol",
    "evolutionary-biology":"evol",
    "paleontology":"evol",
    "plant-biology":"evol",

    "bioengineering":"molcel",
    "bioinformatics":"molcel",
    "systems-biology":"molcel",
    "biophysics":"molcel",
    "synthetic-biology":"molcel",
    "biochemistry":"molcel",
    "cell-biology":"molcel",
    "genetics":"molcel",
    "genomics":"molcel",
    "molecular-biology":"molcel",
    "microbiology":"molcel",
}

# subfields # deprecated
# category_to_subfield = {
#     # Molecular & Cellular Biology
#     "Biochemistry": "MolCel",
#     "Biophysics": "MolCel",
#     "Cell Biology": "MolCel",
#     "Molecular Biology": "MolCel",
#     "Genetics": "MolCel",
#     "Genomics": "MolCel",
#     "Synthetic Biology": "MolCel",
#     "Systems Biology": "MolCel",

#     # Biomedical Sciences
#     "Cancer Biology": "BioMed",
#     "Immunology": "BioMed",
#     "Pathology": "BioMed",
#     "Pharmacology And Toxicology": "BioMed",
#     "Physiology": "BioMed",
#     "Clinical Trials": "BioMed",

#     # Organismal & Behavioral Biology
#     "Animal Behavior And Cognition": "Behav",
#     "Neuroscience": "Behav",
#     "Zoology": "Behav",
#     "Developmental Biology": "Behav",

#     # Ecology & Evolution
#     "Ecology": "Evol",
#     "Evolutionary Biology": "Evol",
#     "Paleontology": "Evol",
#     "Plant Biology": "Evol",

#     # Computational & Interdisciplinary
#     "Bioinformatics": "CompInt",
#     "Bioengineering": "CompInt",
#     "Microbiology": "CompInt",
#     "Epidemiology": "CompInt",
#     "Scientific Communication And Education": "CompInt",
# }

MolCel = [
    1303, 1304, 1305, 1307, 1311, 1312, 1315,
    2402, 2804
]
# Cell Biology: 1307

BioMed = [
    1302, 1306, 1308, 1310, 1313, 1314,
    1502, 2204,
    2403, 2405, 2406,
    # 2704, 2705, 2706, 2707, 2708, 2709, 2710, 2711,
    # 2712, 2714, 2715, 2716, 2717, 2720, 2721, 2722, # 2018, 2019
    # 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730,
    # 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2738,
    # 2740, 2741, 2742, 2743, 2744, 2745, 2746, 2747,
    # 2748,
    3002, 3003, 3004, 3005
]

Behav = [
    1103, 1309, 2702, 2710,
    2802, 2803, 2806,
    3200, 3201, 3202, 3203, 3204, 3205, 3206, 3207
]

Evol = [
    1104, 1105,
    2302, 2303, 2306, 2309
]

# CompInt = [
#     2404, 2713, 2718, 2719  #2739
# ]

Asjcs = {
    "MolCel": MolCel,
    "BioMed": BioMed,
    "Behav": Behav,
    "Evol": Evol,
    # "CompInt": CompInt,
}

"""ASJCS
  1103 Animal Science and Zoology
  1104 Aquatic Science
  1105 Ecology, Evolution, Behavior and Systematics

  1300 Biochemistry, Genetics and Molecular Biology (all)
  1301 Biochemistry, Genetics and Molecular Biology (miscellaneous)
  1302 Aging
  1303 Biochemistry
  1304 Biophysics
  1305 Biotechnology
  1306 Cancer Research
  1307 Cell Biology
  1308 Clinical Biochemistry
  1309 Developmental Biology
  1310 Endocrinology
  1311 Genetics
  1312 Molecular Biology
  1313 Molecular Medicine
  1314 Physiology
  1315 Structural Biology

  1502 Bioengineering
  
  2204 Biomedical Engineering

  2302 Ecological Modeling
  2303 Ecology
  #...
  2306 Global and Planetary Change
  #...
  2309 Nature and Landscape Conservation

  2400 Immunology and Microbiology (all)
  2401 Immunology and Microbiology (miscellaneous)
  2402 Applied Microbiology and Biotechnology
  2403 Immunology
  2404 Microbiology
  2405 Parasitology
  2406 Virology

  # 2700 Medicine (all)
  # 2701 Medicine (miscellaneous)
  # 2702 Anatomy
  # 2703 Anesthesiology and Pain Medicine
  # 2704 Biochemistry (medical)
  # 2705 Cardiology and Cardiovascular Medicine
  # 2706 Critical Care and Intensive Care Medicine
  # 2707 Complementary and Alternative Medicine
  # 2708 Dermatology
  # 2709 Drug Guides
  # 2710 Embryology
  # 2711 Emergency Medicine
  # 2712 Endocrinology, Diabetes and Metabolism
  # 2713 Epidemiology
  # 2714 Family Practice
  # 2715 Gastroenterology
  # 2716 Genetics (clinical)
  # 2717 Geriatrics and Gerontology
  # 2718 Health Informatics ###
  # 2719 Health Policy ###
  # 2720 Hematology
  # 2721 Hepatology
  # 2722 Histology
  # 2723 Immunology and Allergy
  # 2724 Internal Medicine
  # 2725 Infectious Diseases
  # 2726 Microbiology (medical)
  # 2727 Nephrology
  # 2728 Neurology (clinical)
  # 2729 Obstetrics and Gynecology
  # 2730 Oncology
  # 2731 Ophthalmology
  # 2732 Orthopedics and Sports Medicine
  # 2733 Otorhinolaryngology
  # 2734 Pathology and Forensic Medicine
  # 2735 Pediatrics, Perinatology and Child Health
  # 2736 Pharmacology (medical)
  # 2737 Physiology (medical)
  # 2738 Psychiatry and Mental Health
  # 2739 Public Health, Environmental and Occupational Health
  # 2740 Pulmonary and Respiratory Medicine
  # 2741 Radiology, Nuclear Medicine and Imaging
  # 2742 Rehabilitation
  # 2743 Reproductive Medicine
  # 2744 Reviews and References (medical)
  # 2745 Rheumatology
  # 2746 Surgery
  # 2747 Transplantation
  # 2748 Urology

  2800 Neuroscience (all)
  2801 Neuroscience (miscellaneous)
  2802 Behavioral Neuroscience
  2803 Biological Psychiatry
  2804 Cellular and Molecular Neuroscience
  2805 Cognitive Neuroscience
  2806 Developmental Neuroscience
  2807 Endocrine and Autonomic Systems
  2808 Neurology
  2809 Sensory Systems

  3000 Pharmacology, Toxicology and Pharmaceutics (all)
  3001 Pharmacology, Toxicology and Pharmaceutics (miscellaneous)
  3002 Drug Discovery
  3003 Pharmaceutical Science
  3004 Pharmacology
  3005 Toxicology

  3200 Psychology (all)
  3201 Psychology (miscellaneous)
  3202 Applied Psychology
  3203 Clinical Psychology
  3204 Developmental and Educational Psychology
  3205 Experimental and Cognitive Psychology
  3206 Neuropsychology and Physiological Psychology
  3207 Social Psychology
"""