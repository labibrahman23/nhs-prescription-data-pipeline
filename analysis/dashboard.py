import streamlit as st

    

from nhs_pipeline.database import create_connection

from queries import (
    get_dashboard_metrics,
    get_highest_total_cost,
    get_regions_by_total_expenditure,
    get_most_prescribed_by_region,
    get_bnf_chapter_analysis

    
)
from visualisation import (
    plot_region_total_expenditure,
    plot_greatest_costing

)





st.set_page_config(layout="wide", page_title="NHS Prescription Dashboard")

connection = create_connection()


st.markdown("""
    <style>
    .block-container {
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 100%;
    }
    </style>
""", unsafe_allow_html=True)


#Split the dashboard into left and right side 
left_side, right_side = st.columns([1,1.3])

with left_side:
    

    with st.container():
        st.subheader("NHS Prescription Dashboard")
        

        metrics = get_dashboard_metrics(connection)
        col1, col2, col3, col4 = st.columns(4)

    

    with st.container():

        with col1:
            st.metric(" Total NHS Precription Cost ",
            f"£{metrics['total_cost'].iloc[0]:,.0f}"
            )
    
        with col2:
            st.metric(
            "Total number of Prescriptions",
            f"{metrics['total_prescriptions'].iloc[0]:,.0f}"
            )

        with col3:
            st.metric(
            " Medications analysed",
            f"{metrics['number_medications'].iloc[0]:,.0f}"
            )

        with col4:
            st.metric(
            "Regions analysed:",
            f"{metrics['number_regions'].iloc[0]:,.0f}"
            )

    


    with st.container():
        st.subheader("NHS Prescription Expnediture by region")
        #Plot Region by total expenditure 
        df_region_total = get_regions_by_total_expenditure(connection)
        chart_region_total = plot_region_total_expenditure(df_region_total)

        st.plotly_chart(chart_region_total)
        

        with st.expander("About this analysis"):
            st.write("""
            # Why I asked this:
            -NHS can use this to find which regions cost them the most and they could look into reasons as to why 
            -NHS can research into ways on reducing diseases in that area
        
            # My theories:
            -Cost of raw materials for that prescription is high, could use rare materials / imported goods
            """)

    with st.container():
        st.subheader("Which Medical regions need the most prescriptions and funding?")

        df_bnf_analysis = get_bnf_chapter_analysis(connection)

        df_bnf_analysis = df_bnf_analysis.sort_values("total_prescriptions", ascending=False)

        st.dataframe(df_bnf_analysis, use_container_width=True, hide_index=True)




with right_side:

    with st.container():

        st.subheader("Most Prescribed Drugs ")
        #Plot Highest Total cost 
        highest_cost_df = get_highest_total_cost(connection)
        highest_cost_chart = plot_greatest_costing(highest_cost_df)

        st.plotly_chart(highest_cost_chart)
    

    with st.expander("Business Values and Insights "):
        st.markdown("""

        ###Business Value
        -NHS may want to look at the top costing and then look further into its cost ove rmonths / years for the NHS, then look into ways of developing those drugs to be cheaper in production 
        -also whtehrr they are overprescribed - for reasons similar to the first question
        -it also can be used to build reports about which diseases / illnesses are causing the greatest cost for the NHS over years,
        -look at possible tarrifs / cost of importing materials needed in production and see if they can form some deals to help with this as medication is a neccesity
        -find which drugs are the biggest financial risk if prices increase by 20%

        ###Insights
        -new attempts at the drug and usually these are very expensive and reduce in cost of production over time
        -maybe it is not produced in the UK but imported
        -materials needed to produce that drug are rare"
        -High-cost medications may warrant further investigation into prescribing patterns, clinical effectiveness, availability of alternatives, and whether they provide sufficient value relative to their cost

        # Limitations:
        gives overall total cost rather than individual cost per prescription
          cost does not equal inefficiency
          """)   

    with st.container():

        st.subheader("Most Prescribed Drugs by region ")

        df_most_prescribed_per_region = get_most_prescribed_by_region(connection)

        df_most_prescribed_per_region = df_most_prescribed_per_region.sort_values(by='quantity_prescribed', ascending=False)

        st.dataframe(df_most_prescribed_per_region,use_container_width=True, hide_index=True)

        with st.expander("Business Values and Insights "):
            st.markdown("""
            ###Business Value
            Finds which regions prescribe the most of which medication

            -They can use this to further look into which specific diseases / illnesses are affecting certain areas, 
            
            ### Insights
            That area is struggling a lot more than others
            Families carry that disease, genetic

            ### Limitations
            Large regions may dominate the chart
            """)
        

    with st.container():
        st.subheader("Key findings")
    
        

        
        st.write(""""
        - There greatest costing drugs are \n
        - These regions prescribe a lot of ... which could mean they need\n
        - This region uses the most government spenditure, meaning that area could need more focus\n
        - This medical region needs a lot of funding, could need some research\n
        """)

        


