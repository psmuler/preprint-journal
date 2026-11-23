data_path = "/home/ec2-user/r2"
openalex_path = "s3://openalex-bulk"
root = "/disks/qnap4/shared/scopus-25/data/"

# source does not work
preprint_primary_location_ids = {
    "arxiv":"S4306400194",
    "biorxiv":"S4306402567",
    "medrxiv":"S4306400573",
    "osf":"S4306401127",
    "PsyArxiv":"S4306401687",
    "SocArxiv":"S4306401238",
}


"""aws s3 ls s3://openalex-bulk/ --recursive > result.txt
authors/2yr_cited_by_count
authors/2yr_h_index
authors/2yr_i10_index
authors/2yr_mean_citedness
authors/2yr_works_count
authors/affiliations_institution_id
authors/affiliations_institution_lineage
authors/affiliations_institution_years
authors/cited_by_count
authors/concepts_display_name
authors/concepts_id
authors/concepts_level
authors/concepts_score
authors/concepts_wikidata
authors/counts_by_year
authors/created_date
authors/display_name
authors/display_name_alternatives
authors/i10_index
authors/ids
authors/last_known_institution_ids
authors/most_cited_work
authors/oa_percent
authors/orcid
authors/topics_count
authors/topics_id
authors/topics_share
authors/updated_date
authors/works_count
funders/2yr_mean_citedness
funders/alternate_titles
funders/cited_by_count
funders/concepts_display_name
funders/concepts_id
funders/concepts_level
funders/concepts_score
funders/concepts_wikidata
funders/country_code
funders/country_id
funders/counts_by_year
funders/created_date
funders/description
funders/display_name
funders/grants_count
funders/h_index
funders/homepage_url
funders/i10_index
funders/ids
funders/image_thumbnail_url
funders/image_url
funders/role
funders/roles_id
funders/roles_works_count
funders/updated_date
funders/works_count
institutions/2yr_cited_by_count
institutions/2yr_h_index
institutions/2yr_i10_index
institutions/2yr_mean_citedness
institutions/2yr_works_count
institutions/associated_institution_id
institutions/associated_institution_relationship
institutions/cited_by_count
institutions/city
institutions/concepts_display_name
institutions/concepts_id
institutions/concepts_level
institutions/concepts_score
institutions/concepts_wikidata
institutions/country
institutions/country_code
institutions/country_id
institutions/counts_by_year
institutions/created_date
institutions/display_name
institutions/display_name_acronyms
institutions/display_name_alternatives
institutions/geonames_city_id
institutions/h_index
institutions/homepage_url
institutions/i10_index
institutions/ids
institutions/image_thumbnail_url
institutions/image_url
institutions/is_super_system
institutions/latitude
institutions/lineage
institutions/longitude
institutions/oa_percent
institutions/region
institutions/relationship
institutions/repository_id
institutions/role
institutions/roles_id
institutions/roles_works_count
institutions/ror
institutions/topics_count
institutions/topics_id
institutions/topics_share
institutions/type
institutions/type_id
institutions/updated_date
institutions/works_count
publishers/2yr_cited_by_count
publishers/2yr_h_index
publishers/2yr_i10_index
publishers/2yr_mean_citedness
publishers/2yr_works_count
publishers/alternate_titles
publishers/cited_by_count
publishers/concepts_display_name
publishers/concepts_id
publishers/concepts_level
publishers/concepts_score
publishers/concepts_wikidata
publishers/country_codes
publishers/counts_by_year
publishers/created_date
publishers/display_name
publishers/h_index
publishers/hierarchy_level
publishers/homepage_url
publishers/i10_index
publishers/ids
publishers/image_thumbnail_url
publishers/image_url
publishers/lineage
publishers/oa_percent
publishers/parent_publisher_id
publishers/role
publishers/roles_id
publishers/roles_works_count
publishers/sources_count
publishers/updated_date
publishers/works_count
sources/2yr_cited_by_count
sources/2yr_h_index
sources/2yr_i10_index
sources/2yr_mean_citedness
sources/2yr_works_count
sources/abbreviated_title
sources/alternate_titles
sources/apc_prices
sources/apc_usd
sources/cited_by_count
sources/concepts_display_name
sources/concepts_id
sources/concepts_level
sources/concepts_score
sources/concepts_wikidata
sources/country_code
sources/country_id
sources/counts_by_year
sources/created_date
sources/display_name
sources/h_index
sources/homepage_url
sources/host_organization
sources/host_organization_lineage
sources/host_organization_lineage_names
sources/host_organization_name
sources/i10_index
sources/ids
sources/is_core
sources/is_in_doaj
sources/is_indexed_in_scopus
sources/is_oa
sources/issn
sources/issn_l
sources/oa_percent
sources/publisher
sources/publisher_id
sources/publisher_lineage
sources/publisher_lineage_names
sources/societies
sources/topics_count
sources/topics_id
sources/topics_share
sources/type
sources/type_id
sources/updated_date
sources/works_count
works/abstract
works/apc_list
works/apc_paid
works/author_countries
works/author_id
works/author_institutions
works/author_is_corresponding
works/author_position
works/author_raw_affiliation_strings
works/author_works
works/authors_count
works/authors_works
works/authorships_truncated
works/best_oa_location_id
works/best_oa_location_is_oa
works/best_oa_location_landing_page_url
works/best_oa_location_license
works/best_oa_location_pdf_url
works/best_oa_location_version
works/biblio
works/citation_normalized_percentile
works/cited_by_api_url
works/cited_by_count
works/cited_by_percentile_year
works/concepts_count
works/concepts_display_name
works/concepts_id
works/concepts_level
works/concepts_score
works/concepts_wikidata
works/corresponding_author_ids
works/corresponding_institution_ids
works/countries_distinct_count
works/counts_by_year
works/created_date
works/datasets
works/display_name
works/doi
works/doi_registration_agency
works/domains
works/fields
works/fulltext_origin
works/fwci
works/grants
works/has_fulltext
works/ids
works/indexed_in
works/institution_assertions
works/institutions_distinct_count
works/is_oa
works/is_paratext
works/is_retracted
works/keywords
works/language
works/language_id
works/locations_count
works/mesh
works/oa_any_repository_has_fulltext
works/oa_status
works/oa_url
works/open_access
works/primary_location_id
works/primary_location_is_oa
works/primary_location_landing_page_url
works/primary_location_license
works/primary_location_pdf_url
works/primary_location_version
works/primary_topic
works/publication_date
works/publication_year
works/referenced_works
works/referenced_works_count
works/related_works
works/subfields
works/summary_stats
works/sustainable_development_goals
works/title
works/topics_count
works/topics_id
works/topics_score
works/type
works/type_crossref
works/type_id
works/updated
works/updated_date
works/versions
"""



"""
Cell：編集部は「professional in-house editors」のチームと明記（編集記事）。  ￼
Cell Reports： “editorial decisions … are made independently by its in-house scientific editors”“professional in-house editors” と複数箇所で明示。  ￼
Cell Reports Medicine： “professional in-house scientific editors” と明示。  ￼
Cell Reports Physical Science： “Work with professional in-house editors” と明示。  ￼
Cell Reports Sustainability： “professional in-house scientific editors” と明示。  ￼
Cell Systems：投稿規程で “handled by the in-house editorial team”，エディトリアルでも “handled by our in-house team of full-time editors” と明示。  ￼
Cell Metabolism：投稿規程で “handled by the in-house editorial team”，編集長記事で “Cell Metabolism in-house editors and I …” と明記。  ￼
Cell Host & Microbe：投稿規程で “handled by the in-house editorial team”。  ￼
Neuron：投稿規程で “handled by the in-house editorial team”。  ￼
Immunity：投稿規程で “handled by the in-house editorial team”。さらに 2005 年の編集告知で “move to an ‘in-house’ editorial model” と明示。  ￼
Molecular Cell：レビュー移管の記述で “in-house professional editors” と明示。  ￼
Cancer Cell：投稿規程で “handled by the in-house editorial team”。  ￼
Current Biology：Cell（Trends）系の編集ポリシーで，該当誌を含め “handled by the in-house editorial team” と明示。  ￼
Chem：投稿規程で “handled by the in-house editorial team”。  ￼
Chem Catalysis：投稿規程/Why submit で “(in-house) professional editors”。  ￼
Joule：投稿規程で “handled by the in-house editorial team”。  ￼
Matter：投稿規程で “handled by the in-house editorial team”。  ￼
Med：投稿規程で “handled by the in-house editorial team”；Viewpoint は “evaluated by the in-house professional editors”。  ￼
Structure：Why submit で “professional in-house editors”。  ￼
Cell Chemical Biology：Why submit で “professional in-house scientific editors”；編集者紹介にも “in-house editor” と明記。  ￼
Patterns：著者向けページで “In-house professional editors give authors hands-on support” と明記。  ￼
Device：著者向け PDF で “editorial operations … run by professional in-house editors” と明示。  ￼
Heliyon：FAQ／Editors & Staff で “(our) in-house editorial team …” と明記（セクション制）。  ￼
Cell Genomics：Why submit で “team of professional in-house editors”。  ￼
One Earth：編集長記事で “full-time in-house editors attend conferences …” と明示。  ￼
Developmental Cell：投稿規程で “handled by the in-house editorial team”，創刊初期から “in-house editorial team” と自称。
"""

inhouse_titles_v1 = [
    # Cell Press
    "Cell",
    "Cell Reports",
    "Cell Reports Medicine", 
    "Cell Reports Physical Science",
    "Cell Reports Sustainability",
    "Cell Systems",
    "Cell Metabolism",
    "Cell Host & Microbe",
    "Neuron",
    "Immunity",
    "Molecular Cell",
    "Cancer Cell",
    "Current Biology",
    "Chem",
    "Chem Catalysis",
    "Joule",
    "Matter",
    "Med",
    "Structure",
    "Cell Chemical Biology",
    "Patterns",
    "Device",
    "Heliyon",
    "Cell Genomics",
    "One Earth",
    "Developmental Cell",
    
    # Nature Portfolio
    "Nature",
    "Nature Medicine",
    "Nature Biotechnology",
    "Nature Neuroscience",
    "Nature Genetics",
    "Nature Immunology",
    "Nature Reviews Molecular Cell Biology",
    "Nature Reviews Cancer",
    "Nature Aging",
    "Nature Biomedical Engineering",
    "Nature Biotechnology",
    "Nature Cancer",
    "Nature Chemical Biology",
    "Nature Cities",
    "Nature Climate Change",
    "Nature Computational Science",
    "Nature Energy",
    "Nature Food",
    "Nature Machine Intelligence",
    "Nature Mental Health",
    "Nature Human Behaviour",
    "Nature Communications",
    "Nature Reviews Biodiversity",
    "Nature Reviews Cancer",
    "Nature Reviews Clean Technology",
    "Nature Reviews Drug Discovery",
    "Nature Reviews Genetics",
    "Nature Reviews Immunology",
    "Nature Reviews Mircrobiology",
    "Nature Reviews Molecular Cell Biology",
    "Nature Reviews Neuroscience",
    "Nature Sustainability",
    "Nature Reviews Psychology",
    "Nature Water",
    # BMJ
    
    # The Lancet
    # AAAS
    "Science",
    "Science Translational Medicine",
]