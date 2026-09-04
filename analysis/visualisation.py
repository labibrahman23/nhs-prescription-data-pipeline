import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


def plot_greatest_costing(df):

    df = df[::-1]

    fig = px.bar(
        df,
        x = "total_cost",
        y = "prescription",
        orientation = "h",
        text = "total_quantity",
        hover_data = {
            "prescription": True,
            "total_cost" : ":,.0f",
            "total_quantity": "Total Quantity Prescribed"
        },
        labels = {
            "prescription": "Medication",
            "total_cost" : "Total cost to NHS (£)",
            "total_quantity": "Total Quantity Prescribed"
        }

    )

    return fig



def plot_region_total_expenditure(df):

    fig = px.pie(df, values="total_cost", names="region")
    return fig

    
def old_region_by_total_expenditure(df):

    """Plot bar chart for top costing regions """
    df = df.sort_values(by="total_cost", ascending=True)

    fig, ax = plt.subplots(figsize=(10,6))
    
    
    x = df["region"].str[0:7] + ("...")
    y = df["total_cost"]

    ax.set_xlabel("Region")
    ax.set_ylabel("Total Expenditure")
    ax.set_title("Total Prescription Expenditure By Region")

    barlist = ax.bar(x,y)
    for bar in barlist[-3:]:
        bar.set_color('red')
    return fig


def plot_highest_cost(df):

    """Create horizontal bar chart for greatest total costing prescriptions to NHS"""
    

    fig, ax = plt.subplots(figsize=(10,6))

    df = df.sort_values(by = 'total_cost', ascending = True)



    short_prescription = df["prescription"].str[0:20] + ("...")
    y = short_prescription
    x = df["total_cost"]
    barlist = ax.barh(y,x)
    for bar in barlist[-3:]:
        bar.set_color('red')

    ax.set_xlabel("Total Cost")
    ax.set_ylabel("prescription")
    ax.set_title("Greatest Total Cost to NHS")
    return fig

def plot_region_to_medication(df):

    """Create horizontal bar chart for top medications prescribed per region"""

    fig, ax = plt.subplots(figsize=(10,6))
    
    df = df.sort_values(by = 'total_orders', ascending = True)
    short_prescription = df["prescription"].str[0:15] + ("...")
    df["region_to_medication"] = (

        df["region"] + ("...") + short_prescription
    )

    y = df["region_to_medication"]
    x = df["total_orders"]
    barlist = ax.barh(y,x)
    for bar in barlist[-3:]:
        bar.set_color('red')
    ax.set_xlabel("Total Orders")
    ax.set_ylabel("Region - Medication")
    ax.set_title("Medication Prescribed by Region")
    return fig

def plot_medication_volume_to_cost(df):

    """Create scatter graph to show relationship between cost and volume, between top prescriptions """

    fig, ax = plt.subplots(figsize=(8,5))
    
    highest_cost = df.nlargest(10,"total_cost")
    highest_quantity = df.nlargest(10,"total_quantity")


    df = pd.concat([highest_cost,highest_quantity]).drop_duplicates()
    
    x = df["total_quantity"]
    y = df["total_cost"]

    ax.set_xlabel("Total Quantity Prescribed")
    ax.set_ylabel("Total Cost")
    ax.set_title("Prescription Quantity to Cost Relationship")

    ax.scatter(x,y)
    return fig

def plot_highest_prescribed_drugs(df):

    """Create a horizontal bar chart for the most prescribed drugs """

    fig, ax = plt.subplots(figsize=(10,6))
    df = df.sort_values(by = 'total_quantity_prescribed', ascending = True)

    prescription_names_short = df["prescription"].str[:20] + "..."

    y = prescription_names_short
    x = df["total_quantity_prescribed"]
    
    barlist = ax.barh(y,x)
    for bar in barlist[-3:]:
        bar.set_color('red')

    ax.set_xlabel("Total Quantity Prescribed")
    ax.set_ylabel("prescription")
    ax.set_title("Most Prescribed Drugs UK")
    return fig




"""connection = create_connection()

df = get_highest_prescribed_drugs(connection)
plot_highest_prescribed_drugs(df)

df = get_highest_total_cost(connection)
plot_highest_cost(df)

df = get_region_to_medication(connection)
plot_region_to_medication(df)

df = get_medication_cost_volume_relationship(connection)
plot_medication_volume_to_cost(df)

df =  get_regions_by_total_expenditure(connection)
plot_region_total_expenditure(df)"""


"""
from queries import get_highest_prescribed_drugs
from queries import get_highest_total_cost
from queries import get_region_to_medication
from queries import get_medication_cost_volume_relationship
from queries import get_regions_by_total_expenditure
from database import create_connection"""
