"""
Business Questions

1. Which medications have the highest total prescribed quantity?
2. Which medications contribute most to NHS prescription expenditure?
3. Which region-medication combinations have the highest prescription volume?
4. What is the relationship between medication cost and prescription volume?
5. Which NHS regions account for the greatest prescription expenditure?

"""

import pandas as pd



def get_dashboard_metrics(connection):

    """ Get metrics for Dashboard """
    query = """
    SELECT SUM(actual_cost) as total_cost,
    SUM(items) as total_prescriptions,
    COUNT(DISTINCT bnf_presentation_name) as number_medications,
    COUNT(DISTINCT regional_office_name) as number_regions
    FROM prescriptions
    WHERE bnf_presentation_name != 'Exception Handler Discount Not Deducted Item';
    """

    return pd.read_sql(query,connection)

def get_highest_total_cost(connection):

    """ Get highest total costing drugs to NHS """

    query = """
       SELECT bnf_presentation_name as prescription, SUM(total_quantity) as total_quantity, SUM(actual_cost) as total_cost
       FROM prescriptions
       WHERE bnf_presentation_name != 'Exception Handler Discount Not Deducted Item'
       GROUP BY bnf_presentation_name
       ORDER BY total_cost DESC
       LIMIT 10;
       """

    return pd.read_sql(query,connection)



def get_most_prescribed_by_region(connection):

    """Get total expenditure  per region """
    query = """
    SELECT region, Medication, quantity_prescribed, total_cost, bnf_chapter_plus_code
    FROM(
        SELECT regional_office_name as region, bnf_presentation_name as Medication, SUM(items) as quantity_prescribed, sum(actual_cost) as total_cost, bnf_chapter_plus_code,
        ROW_NUMBER() OVER ( PARTITION BY regional_office_name ORDER BY SUM(items) DESC )as ranked
    FROM prescriptions
    WHERE bnf_presentation_name != 'Exception Handler Discount Not Deducted Item'
    GROUP BY regional_office_name, bnf_presentation_name, bnf_chapter_plus_code) as ranked_medications
    WHERE ranked = 1;
    """

    return pd.read_sql(query,connection)


#Which NHS regions account for the greatest prescription expenditure?"
def get_regions_by_total_expenditure(connection):

    """Get total expenditure  per region """
    query = """
    SELECT regional_office_name as region, sum(actual_cost) as total_cost
    FROM prescriptions
    WHERE bnf_presentation_name != 'Exception Handler Discount Not Deducted Item'
    GROUP BY regional_office_name
    ORDER BY total_cost DESC;
    """

    return pd.read_sql(query,connection)


def get_bnf_chapter_analysis(connection):

    query = """
    SELECT bnf_chapter_plus_code, SUM(items) as total_prescriptions, SUM(actual_cost) as total_cost
    FROM prescriptions
    WHERE bnf_presentation_name != 'Exception Handler Discount Not Deducted Item'
    GROUP BY bnf_chapter_plus_code
    ORDER BY total_prescriptions DESC;
    """

    return pd.read_sql(query,connection)




#Additonal queries:


def get_highest_prescribed_drugs(connection):

    """ Get most prescribed drugs """

    query = """
    SELECT bnf_presentation_name as prescription, sum(total_quantity) AS total_quantity_prescribed
    FROM prescriptions
    WHERE NOT bnf_presentation_name = 'Exception Handler Discount Not Deducted Item'
    GROUP BY bnf_presentation_name
    ORDER BY total_quantity_prescribed DESC
    LIMIT 10
    ;
    """

    return pd.read_sql(query,connection)





def get_region_to_medication(connection):

    """ Get most prescribed drugs per region """
    
    query = """
    SELECT regional_office_name as region, bnf_presentation_name as prescription, SUM(items) as total_orders
    FROM prescriptions
    WHERE bnf_presentation_name != 'Exception Handler Discount Not Deducted Item'
    GROUP BY regional_office_name, bnf_presentation_name
    ORDER BY total_orders DESC
    LIMIT 15;
    """
    return pd.read_sql(query,connection)

def get_medication_cost_volume_relationship(connection):

    """Get relationship between medication cost and prescription volume """
    query = """
    SELECT bnf_presentation_name as prescription, SUM(total_quantity) as total_quantity, SUM(actual_cost) as total_cost
    FROM prescriptions
    WHERE bnf_presentation_name != 'Exception Handler Discount Not Deducted Item'
    GROUP BY bnf_presentation_name
    ORDER BY total_cost DESC
    LIMIT 10;
    """

    return pd.read_sql(query,connection)


