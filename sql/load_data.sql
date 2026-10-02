

COPY prescriptions (
    year_month,
    regional_office_name,
    regional_office_code,
    icb_name,
    icb_code,
    pco_name,
    pco_code,
    practice_name,
    practice_code,
    postcode,
    bnf_chemical_substance_code,
    bnf_chemical_substance,
    bnf_presentation_code,
    bnf_presentation_name,
    bnf_chapter_plus_code,
    quantity,
    items,
    total_quantity,
    adq_usage,
    nic,
    actual_cost,
    unidentified,
    snomed_code
    )
FROM STDIN
WITH (
    FORMAT CSV,
    HEADER TRUE
);
            