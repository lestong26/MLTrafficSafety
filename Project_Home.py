import streamlit as st

st.image('images/title.png')
st.caption('Group 1 Exp1orers - Francesca Panga | Jacob Fuentebella | Jersy Carino | Leonard Inciso | Lester Covarrubias II')

st.title ('Introduction')

# Display justified text using HTML/CSS within markdown
st.markdown(
    """
    <div style="text-align: justify">
        Approximately 1.19 million people lose their lives each year due to road traffic crashes globally. This alarming statistic underscores the urgent need for effective measures to address road safety issues. 92% of global road deaths occur in low- and middle-income countries, which account for just 60% of the world's vehicles. This disparity highlights the critical importance of prioritizing road safety initiatives, particularly in regions with limited resources, including the Philippines. Over the past decade, our country has seen a rise in road traffic accidents. In 2023 alone, Metro Manila recorded around 86,000 accidents, a 20% increase from the previous year, with 14% resulting in fatalities. These incidents not only impact lives but also cost 2.6% of the country's GDP, highlighting the economic burden of road safety issues. Aligned with Sustainable Development Goal (SDG) #3, "Good Health and Well-being," and SDG #11, "Sustainable Cities and Communities", our study on enhancing road safety through machine learning is crucial, as road traffic accidents significantly threaten public health and well-being globally.
    </div>
    """,
    unsafe_allow_html=True
)
st.write('---')

st.header('Scope', divider='blue')
st.markdown(
    """
    <div style="text-align: justify">
        Our research focuses on road accidents from 2018 to 2020 within Metro Manila given its significant number of vehicular accidents. We aim to create a binary classification Machine Learning model that determines if a specific accident is a self-accident or not a self-accident. Self-accidents are single-vehicle accidents typically caused by road hazards (potholes, uneven road surface, misaligned barriers, poorly maintained infrastructure), speeding, distracted/reckless driving, or poor weather conditions. These are often underreported due to its nature being a minor incident. We want to detect these accidents to provide local government units (LGUs) with actionable insights to improve road safety. The goal is to find the model that optimizes precision score, as it is our aim to detect the most true positives as possible.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """


    """
)
st.markdown(
    """
    <div style="text-align: justify">
        The map below categorizes all vehicular accidents as gray points, while red points show where self-accidents occur (plotted such that areas with denser self-accident occurences show as larger points).
    </div>
    """,
    unsafe_allow_html=True
)

st.image('images/mmda_geopandas.png')
st.write('---')


st.header('Objectives', divider='blue')
st.subheader('Our objectives are:')
st.image('images/objectives.png')
st.write('---')

st.header('Methodology', divider='blue')
st.image('images/methodology.png')
         
st.markdown(
    """
    <div style="text-align: justify">
        For our methodology, we began by understanding our problem, followed by thorough data cleaning and preprocessing. Before conducting exploratory data analysis, we first identified outliers but ultimately decided to keep them. After preparing our final dataset, we initiated the modeling process. This involved creating a baseline model and iterating through various combinations of hypertuning and resampling. We then interpreted the results using SHAP force plots, beeswarm plots, and LIME prediction probability. Finally, based on the insights gathered, we came up with our recommendations and initialized our deployment through Streamlit.
    </div>
    """,
    unsafe_allow_html=True
)
