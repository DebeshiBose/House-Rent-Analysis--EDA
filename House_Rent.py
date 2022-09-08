import pandas as pd
import plotly.express as px
import streamlit as st
import time

# Side Bar
my_bar = st.progress(100)
for percent_complete in range(100):
     time.sleep(0)
     my_bar.progress(percent_complete + 1)

#Title at the top in bold
st.title(" 🏡 House Rent Analysis Using Plotly ")

st.subheader("This is the DataFrame which has been used to create visual charts 👩‍💻")
df = pd.read_csv('..\\House_Rent_Dataset.csv')

#Displaying the DataFrame
st.dataframe(df)

#Creating dropdown
st.markdown("Lets see few of the possible charts made out of our understanding")
select= ['Pie',"Bar", "Scatter", "Histogram", "Box"]
visuals = st.selectbox(
     'Which visualization do you want to see ?',options=select)
st.write('You selected:', visuals)

# Putting the charts under conditions

if visuals== 'Box':
        fig = px.box(df, x='City', y='Rent', height=500, width=2000, facet_col='BHK', color_discrete_sequence=['black'])
        fig.update_layout(title='Rent of Each City On Basis of BHK', template='simple_white', title_x=0.01,
                          title_font_color="grey")
        st.plotly_chart(fig)
        st.header("This shows the outliers in each cities according to the Rent")

elif visuals== 'Pie':
        ax = df[(df['Rent'] > 20000) & (df['Size'] < 700)]
        fig1 = px.pie(ax, values='Rent', names='City', color_discrete_sequence=px.colors.sequential.Rainbow,
                      title='Filtered Rent paid X City Wise')
        st.plotly_chart(fig1)
        st.header("This shows Rent paid more than 20K for less than 700 SqFt area City wise")
elif visuals == 'Bar':
        ax1 = df.groupby('Tenant Preferred').count()
        fig2 = px.bar(ax1, y='Size', color_discrete_sequence=['goldenrod'],
                      template='simple_white',
                      title='Tenant Preference for Rent',
                      text_auto=True)
        fig2.update_layout(title_x=0.5,
                           font_family='Times New Roman',
                           font_size=15)
        st.plotly_chart(fig2)
        st.header("This shows the total number for Furnished/ Unfurnished/ Semi-Furnished flats for Rent")
elif visuals=='Scatter':
        fig3 = px.scatter(df, df['Rent'], df["Area Locality"], color='Rent', size="Rent", template='simple_white')

        fig3.add_annotation(x=3500000, y=970,
                            text="Most Rent paid",
                            showarrow=True,
                            arrowhead=1,
                            font=dict(
                                family="sans serif",
                                size=18,
                                color="#ffffff"),
                            align="center",
                            arrowsize=1,
                            arrowwidth=2,
                            arrowcolor="#636363",
                            ax=40,
                            ay=-50,
                            bordercolor="#c7c7c7",
                            borderwidth=2,
                            borderpad=4,
                            bgcolor="#ff7f0e",
                            opacity=0.8
                            )
        st.plotly_chart(fig3)
        st.header("This shows the sie of Rent paid in various locality")
        st.markdown("It also shows the most paid rent(which was the outlier) in the city of Bangalore")
else:
        fig4 = px.histogram(df, x="Furnishing Status", y="Rent",
                            color='City', barmode='group',
                            height=500,
                            text_auto=True, template='simple_white')
        st.plotly_chart(fig4)


# Code for understanding
if st.button('Show Code'):
     st.write('Here we go...')
     code = '''import pandas as pd
     import plotly.express as px
     import streamlit as st

     #Title at the top in bold
     st.title(" 🏡 House Rent Analysis Using Plotly ")

     st.subheader("Lets see a glimpse of the DataFrame we are going to visualize 👩‍💻")
     df = pd.read_csv(r'C:\Debeshi\Downloads\House_Rent_Dataset.csv')

     #Displaying the DataFrame
     st.dataframe(df)

     #Creating dropdown
     st.markdown("Lets see few of the possible charts made out of our understanding")
     select= ['Pie',"Bar", "Scatter", "Histogram", "Box"]
     visuals = st.selectbox(
          'Which visualization do you want to see ?',options=select)
     st.write('You selected:', visuals)

     # Putting the charts under conditions
     if visuals== 'Box':
             fig = px.box(df, x='City', y='Rent', height=500, width=2000, facet_col='BHK', color_discrete_sequence=['black'])
             fig.update_layout(title='Rent of Each City On Basis of BHK', template='simple_white', title_x=0.01,
                               title_font_color="grey")
             st.plotly_chart(fig)
             st.header("This shows the outliers in each cities according to the Rent")

     elif visuals== 'Pie':
             ax = df[(df['Rent'] > 20000) & (df['Size'] < 700)]
             fig1 = px.pie(ax, values='Rent', names='City', color_discrete_sequence=px.colors.sequential.Rainbow,
                           title='Filtered Rent paid X City Wise')
             st.plotly_chart(fig1)
             st.header("This shows Rent paid more than 20K for less than 700 SqFt area City wise")
     elif visuals == 'Bar':
             ax1 = df.groupby('Tenant Preferred').count()
             fig2 = px.bar(ax1, y='Size', color_discrete_sequence=['goldenrod'],
                           template='simple_white',
                           title='Tenant Preference for Rent',
                           text_auto=True)
             fig2.update_layout(title_x=0.5,
                                font_family='Times New Roman',
                                font_size=15)
             st.plotly_chart(fig2)
             st.header("This shows the total number for Furnished/ Unfurnished/ Semi-Furnished flats for Rent")
     elif visuals=='Scatter':
             fig3 = px.scatter(df, df['Rent'], df["Area Locality"], color='Rent', size="Rent", template='simple_white')

             fig3.add_annotation(x=3500000, y=970,
                                 text="Most Rent paid",
                                 showarrow=True,
                                 arrowhead=1,
                                 font=dict(
                                     family="sans serif",
                                     size=18,
                                     color="#ffffff"),
                                 align="center",
                                 arrowsize=1,
                                 arrowwidth=2,
                                 arrowcolor="#636363",
                                 ax=40,
                                 ay=-50,
                                 bordercolor="#c7c7c7",
                                 borderwidth=2,
                                 borderpad=4,
                                 bgcolor="#ff7f0e",
                                 opacity=0.8
                                 )
             st.plotly_chart(fig3)
             st.header("This shows the sie of Rent paid in various locality")
             st.markdown("It also shows the most paid rent(which was the outlier) in the city of Bangalore")
     else:
             fig4 = px.histogram(df, x="Furnishing Status", y="Rent",
                                 color='City', barmode='group',
                                 height=500,
                                 text_auto=True, template='simple_white')
             st.plotly_chart(fig4)'''
     st.code(code, language="python")

else:
     st.write('You can see the code here')
















