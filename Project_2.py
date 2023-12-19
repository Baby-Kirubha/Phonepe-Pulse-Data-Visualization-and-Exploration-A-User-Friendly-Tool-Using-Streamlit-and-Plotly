#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Once created the clone of GIT-HUB repository then,
#Required libraries for the program

import pandas as pd
import json
import os
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
SELECT=option_menu(
    menu_title=None,
    options=["phonepe","Home","Explore Data","Findings of project"],
    icons=["phone","house","bar-chart","book"],
    default_index=2,
    orientation="horizontal",
    styles={"container":{"padding":"0!important","background-color":"white","size":"cover","width":"100%"},
            "icon":{"color":"black","font-size":"20px"},
            "nav-link":{"font-size":"20px","test-align":"center","margin":"-2px","--hover-color":"#6F36AD"},
            "nav-link-selected":{"background-color":"#6F36ADj"}})
#findings of project
if SELECT=="Findings of project":
    st.sidebar.title(":red[Findings  of Phonepe Pulse Data Visualization and Exploration]")
    image = Image.open(r"C:\Users\babyk\OneDrive\Pictures\gif\download.jpeg")
    st.sidebar.image(image, use_column_width=True)
    st.sidebar.write('# Insights Discovery:')
    st.sidebar.write('Data visualization helps in uncovering patterns, trends, and insights that might not be apparent in raw data.')
    st.sidebar.write('It can reveal correlations, anomalies, or customer behavior that can inform business decisions.')
    st.title("Findings of the project")
    st.divider()
    st.write("*  Expanding merchant acceptance")
    st.divider()
    st.write("* Digital Transaction Penetration has Grown Unevenly Across States; Higher Penetration in Southern and Western India")
    st.divider()
    st.write('''* Apart from payments, PhonePe integrates various other services like 
             insurance,  merchant transactions, providing users with a comprehensive financial ecosystem.''')
    st.divider()
    st.write('''*  Urban and Rural Adoption''')
if SELECT=="phonepe":
     image = Image.open(r"C:\Users\babyk\OneDrive\Pictures\gif\phonephe.jpeg")
     st.sidebar.image(image, use_column_width=True)
     image2=Image.open(r"C:\Users\babyk\OneDrive\Pictures\Screenshots\Screenshot (54).png")
     st.sidebar.image(image2, use_column_width=True)
     st.title(":violet[PhonePe]")
     st.write(''':violet[PhonePe is an Indian digital payments and financial services company headquartered in Bengaluru,
               Karnataka, India.PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe 
              app, based on the Unified Payments Interface (UPI), went live in August 2016.The PhonePe app is available in 11 
              Indian languages. Using PhonePe, users can send and receive money, recharge mobile, DTH, data cards, 
              make utility payments, pay at shops, invest in tax saving funds, buy insurance, mutual funds, and digital gold.PhonePe 
              is accepted as a payment option by over 3.6 crore offline and online merchant outlets, constituting 99percent of pin codes
               in the country. The app served more than 10 crore users as of June 2018, processed 500 crore transactions by December
               2019, and crossed 10 crore transactions a day in April 2022. It currently has over 50 crore registered users with over
               20 crore monthly active users.PhonePe is licensed by the Reserve Bank of India for the issuance and operation of a 
              Semi Closed Prepaid Payment system.]''')
     

#This is to direct the path to get the data as states
if SELECT=="phonepe" and st.sidebar.button("Uploading from pulse"):
    path1="pulse/data/aggregated/transaction/country/india/state/"
    Agg_state_list=os.listdir(path1)
    #Agg_state_list--> to get the list of states in India

    #<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

    #This is to extract the data's to create a dataframe

    clm1={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}
    for i in Agg_state_list:
        p_i=path1+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                A=json.load(Data)
                for z in A['data']['transactionData']:
                    Name=z['name']
                    count=z['paymentInstruments'][0]['count']
                    amount=z['paymentInstruments'][0]['amount']
                    clm1['Transacion_type'].append(Name)
                    clm1['Transacion_count'].append(count)
                    clm1['Transacion_amount'].append(amount)
                    clm1['State'].append(" ".join(state.capitalize() for state in i.split("-")))
                    clm1['Year'].append(j)
                    clm1['Quater'].append(int(k.strip('.json')))
    #Succesfully created a dataframe
    Agg_Trans_of_state=pd.DataFrame(clm1)


    #This is to direct the path to get the data as states
    #user details 

    path2="pulse/data/aggregated/user/country/india/state/"
    Agg_user_list=os.listdir(path2)



    clm2={'State':[], 'Year':[],'Quater':[],'Brands':[], 'Transacion_count':[], 'Percentage':[]}
    for i in Agg_user_list:
        p_i=path2+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                B=json.load(Data)

                try:
                    for z in B['data']['usersByDevice']:
                        brand=z['brand']
                        count=z['count']
                        percentage=z['percentage']
                        clm2['Brands'].append(brand)
                        clm2['Transacion_count'].append(count)
                        clm2['Percentage'].append(percentage)
                        clm2['State'].append(" ".join(state.capitalize() for state in i.split("-")))
                        clm2['Year'].append(j)
                        clm2['Quater'].append(int(k.strip('.json')))
                except:
                    pass
                
    #Succesfully created a dataframe

    Agg_state_user=pd.DataFrame(clm2)


    # In[4]:





    # In[5]:


    #This is to direct the path to get the data as districts
    #transaction details 

    path3="pulse/data/map/transaction/hover/country/india/state/"
    map_trans_list=os.listdir(path3)


    clm3={'State':[], 'Year':[],'Quater':[],'District':[], 'Transacion_count':[], 'Transaction_amount':[]}
    for i in map_trans_list:
        p_i=path3+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                C=json.load(Data)
                for z in C['data']['hoverDataList']:
                    District=z['name']
                    count=z['metric'][0]['count']
                    Amount=z['metric'][0]['amount']
                    clm3['District'].append(District)
                    clm3['Transacion_count'].append(count)
                    clm3['Transaction_amount'].append(Amount)
                    clm3['State'].append(" ".join(state.capitalize() for state in i.split("-")))
                    clm3['Year'].append(j)
                    clm3['Quater'].append(int(k.strip('.json')))
                
    #Succesfully created a dataframe

    Map_state_trans=pd.DataFrame(clm3)


    # In[6]:





    # In[7]:


    #This is to direct the path to get the data as districts
    #user details 

    path4="pulse/data/map/user/hover/country/india/state/"
    map_user_list=os.listdir(path4)


    clm4={'State':[], 'Year':[],'Quater':[],'District':[], 'Registered_users':[], 'app_opens':[]}
    for i in map_user_list:
        p_i=path4+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                for z in D['data']['hoverData'].items():
                    District=z[0]
                    registeredUsers=z[1]['registeredUsers']
                    appOpens=z[1]['appOpens']
                    clm4['District'].append(District)
                    clm4['Registered_users'].append(registeredUsers)
                    clm4['app_opens'].append(appOpens)
                    clm4['State'].append(" ".join(state.capitalize() for state in i.split("-")))
                    clm4['Year'].append(j)
                    clm4['Quater'].append(int(k.strip('.json')))


    #Succesfully created a dataframe

    Map_state_user=pd.DataFrame(clm4)


    # In[8]:





    # In[9]:


    #This is to direct the path to get the top districts
    #transaction details 

    path5="pulse/data/top/transaction/country/india/state/"
    top_trans_list=os.listdir(path5)


    clm5={'State':[], 'Year':[],'Quater':[],'District':[],'Type':[], 'Count':[], 'Amount':[]}
    for i in top_trans_list:
        p_i=path5+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                E=json.load(Data)
                for z in E['data']['districts']:
                    District=z['entityName']
                    Type=z['metric']['type']
                    count=z['metric']['count']
                    Amount=z['metric']['amount']
                    clm5['District'].append(District)
                    clm5['Type'].append(Type)
                    clm5['Count'].append(count)
                    clm5['Amount'].append(Amount)
                    clm5['State'].append(" ".join(state.capitalize() for state in i.split("-")))
                    clm5['Year'].append(j)
                    clm5['Quater'].append(int(k.strip('.json')))
                    
                
    top_trans=pd.DataFrame(clm5)


    # In[10]:





    # In[11]:


    #This is to direct the path to get the top districts
    #user details 

    path6="pulse/data/top/user/country/india/state/"
    top_trans_list=os.listdir(path6)



    clm6={'State':[], 'Year':[],'Quater':[],'District':[],'Registered_users':[]}
    for i in top_trans_list:
        p_i=path6+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                E=json.load(Data)
                for z in E['data']['districts']:
                    District=z['name']
                    Registered_user=z['registeredUsers']
                    clm6['District'].append(District)
                    clm6['Registered_users'].append(Registered_user)
                    clm6['State'].append(" ".join(state.capitalize() for state in i.split("-")))
                    clm6['Year'].append(j)
                    clm6['Quater'].append(int(k.strip('.json')))

    top_user=pd.DataFrame(clm6)


    # In[12]:





    # In[ ]:





    # In[13]:


    import pymysql


    # In[14]:


    myconnection=pymysql.connect(host="127.0.0.1",user="root",passwd="11721200#Baby")
    cur=myconnection.cursor()


    # In[15]:


    cur.execute("create database if not exists pro2")
    myconnection=pymysql.connect(host="127.0.0.1",user="root",passwd="11721200#Baby",database="pro2")
    cur=myconnection.cursor()


    # In[16]:


    cur.execute('''create table if not exists Aggregate_state_transaction (State text,Year int,Quater int,Transacion_type text,
    Transacion_count int,Transacion_amount int)''')


    # In[17]:


    tab1='''insert ignore into Aggregate_state_transaction (State,Year,Quater,Transacion_type,Transacion_count,Transacion_amount)
    values(%s,%s,%s,%s,%s,%s)'''


    # In[18]:


    for i in range(0,len(Agg_Trans_of_state)):
        cur.execute(tab1,tuple(Agg_Trans_of_state.iloc[i]))
        myconnection.commit()


    # In[22]:


    cur.execute('''create table if not exists Aggregate_state_user_list (State text,Year int,Quater int,Brands text,
    Transacion_count int,Percentage float(30))''')


    # In[23]:


    tab2='''insert ignore into Aggregate_state_user_list(State,Year,Quater,Brands,Transacion_count,Percentage)values(%s,%s,%s,%s,%s,
    %s)'''


    # In[24]:


    for i in range(0,len(Agg_state_user)):
        cur.execute(tab2,tuple(Agg_state_user.iloc[i]))
        myconnection.commit()


    # In[26]:


    cur.execute('''create table if not exists Map_state_transaction (State text,Year int,Quater int,District text,
    Transacion_count int,Transaction_amount int)''')


    # In[27]:


    tab3='''insert ignore into Map_state_transaction (State,Year,Quater,District,Transacion_count,Transaction_amount)
    values(%s,%s,%s,%s,%s,%s)'''


    # In[28]:


    for i in range(0,len(Map_state_trans)):
        cur.execute(tab3,tuple(Map_state_trans.iloc[i]))
        myconnection.commit()


    # In[29]:


    cur.execute('''create table if not exists Map_user_list (State text,Year int,Quater int,District text,
    Registered_users int,app_opens int)''')


    # In[30]:


    tab4='''insert ignore into Map_user_list(State,Year,Quater,District,Registered_users,app_opens)values(%s,%s,%s,%s,%s,%s)'''


    # In[31]:


    for i in range(0,len(Map_state_user)):
        cur.execute(tab4,tuple(Map_state_user.iloc[i]))
        myconnection.commit()


    # In[19]:


    cur.execute('''create table if not exists Top_transaction(State text,Year int,Quater int,
    District text,Type text,Count int,Amount int)''')


    # In[20]:


    tab5='''insert ignore into Top_transaction(State,Year,Quater,District,Type,Count,Amount)values(%s,%s,%s,%s,%s,%s,%s)'''


    # In[21]:


    for i in range(0,len(top_trans)):
        cur.execute(tab5,tuple(top_trans.iloc[i]))
        myconnection.commit()


    # In[22]:


    cur.execute('''create table if not exists Top_user(State text,Year int,Quater int,District text,Registered_users int)''')


    # In[26]:


    tab6='''insert ignore into Top_user(State,Year,Quater,District,Registered_users)values(%s,%s,%s,%s,%s)'''


    # In[27]:


    for i in range(0,len(top_user)):
        cur.execute(tab6,tuple(top_user.iloc[i]))
        myconnection.commit()
#for geo visualisation
import pymysql
import pandas as pd
myconnection=pymysql.connect(host="127.0.0.1",user="root",passwd="11721200#Baby")
cur=myconnection.cursor()
myconnection=pymysql.connect(host="127.0.0.1",user="root",passwd="11721200#Baby",database="pro2")
cur=myconnection.cursor()
if SELECT=="Home":
     st.sidebar.header("Chose your filter")
     details=st.sidebar.selectbox("select details you want to view",("select","Transaction details","Transaction Count","User details"))
     year=st.sidebar.selectbox("select the year",("select",2018,2019,2020,2021,2022,2023))
     quater=st.sidebar.selectbox("select the quater",("select",1,2,3,4))
     if details=="Transaction details" and st.sidebar.button("Extract Data"):
            if year==2023 and quater==4:
                 st.warning("Fourth quater was not updated")
            else:
                query1=f'''select State,sum(Transacion_amount ) from aggregate_state_transaction where Year={year} and 
                        Quater={quater}   group by State;  '''
                cur.execute(query1)
                myconnection.commit()
                d1=cur.fetchall()
                df=pd.DataFrame(d1,columns=["state","Transaction amount"])
                df = df.astype({"Transaction amount":float})
                query2=f'''select sum(Transacion_amount)as total  from aggregate_state_transaction where Year={year} 
                and Quater={quater} group by  Year,Quater;  '''
                cur.execute(query2)
                myconnection.commit()
                d2=cur.fetchall()
                df2=pd.DataFrame(d2,columns=["Total Transaction amount"]) 
                st.dataframe(df2)                    
                import plotly.express as px
                fig = px.choropleth(
                    df,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='state',
                    color='Transaction amount',
                    color_continuous_scale="darkmint"
                )

                fig.update_geos(fitbounds="locations", visible=False)
                fig.update_layout(width=1000,height=800)
                
                st.plotly_chart(fig)
     if details=="Transaction Count" and st.sidebar.button("Extract Data"):
            if year==2023:
                 st.warning("Data is not updated")
            if  year==2022 and  (quater==2 or quater==3 or quater==4):
                 st.warning("Data is not updated")
            else:
                query1=f'''select State,sum(Transacion_count ) from aggregate_state_user_list where Year={year} and 
                        Quater={quater}   group by State;  '''
                cur.execute(query1)
                myconnection.commit()
                d1=cur.fetchall()
                df=pd.DataFrame(d1,columns=["state","Transaction count"])
                df = df.astype({"Transaction count":float})
                query2=f''' select sum(Transacion_count)as total  from aggregate_state_user_list where Year={year} and
                  Quater={quater} group by  Year,Quater; '''
                cur.execute(query2)
                myconnection.commit()
                d2=cur.fetchall()
                df2=pd.DataFrame(d2,columns=["Total Transaction count"])
                df2 = df2.astype({"Total Transaction count":float})
                st.dataframe(df2)                
                import plotly.express as px
                fig = px.choropleth(
                    df,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='state',
                    color='Transaction count',
                    color_continuous_scale="sunsetdark"
                )

                fig.update_geos(fitbounds="locations", visible=False)
                fig.update_layout(width=1000,height=800)
                
                st.plotly_chart(fig)
     if details=="User details" and st.sidebar.button("Extract Data"):
            if year==2023 and quater==4:
                 st.warning("Data is not updated")
            else:
                query1=f'''select state,sum(Registered_users)  from map_user_list where year={year} and quater={quater} group by state; '''
                cur.execute(query1)
                myconnection.commit()
                d1=cur.fetchall()
                df=pd.DataFrame(d1,columns=["state","Registered users"])
                df = df.astype({"Registered users":float})
                query2=f''' select sum(Registered_users)  from map_user_list where year={year} and quater={quater} group by year ,quater; '''
                cur.execute(query2)
                myconnection.commit()
                d2=cur.fetchall()
                df2=pd.DataFrame(d2,columns=["Total no.of Registered users"])
                df2 = df2.astype({"Total no.of Registered users":float})
                st.dataframe(df2)                
                import plotly.express as px
                fig = px.choropleth(
                    df,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='state',
                    color='Registered users',
                    color_continuous_scale="Viridis"
                )

                fig.update_geos(fitbounds="locations", visible=False)
                fig.update_layout(width=1000,height=800)
                
                st.plotly_chart(fig) 
if SELECT=="Explore Data":
     slideryear=st.slider("Select the year", 2018, 2023, value=2018, step=1)
     if st.sidebar.button("Transaction count"):
          if slideryear in[2018,2019,2020,2021]:
            query=f'''select State,sum(Transacion_count)from aggregate_state_user_list where Year={slideryear}
              group by State  order by sum(Transacion_count) desc limit 10; '''
            cur.execute(query)
            myconnection.commit()
            d2=cur.fetchall()
            df=pd.DataFrame(d2,columns=["state","Transaction count"])
            df = df.astype({"Transaction count":float})
            st.title('Top ten States of the year')
            st.header('with respect of transaction count')
            st.bar_chart(data=df,x="state",y="Transaction count")
          elif slideryear==2022 or 2023:
               st.warning("Data not updated")
     if st.sidebar.button(" Dis based on trans_amt"):
        import plotly.express as px
        query=f'''select District ,sum(Transaction_amount) from map_state_transaction where year={slideryear}
          group by State,District order by sum(Transaction_amount) desc limit 10 ;'''
        cur.execute(query)
        myconnection.commit()
        d2=cur.fetchall()
        df=pd.DataFrame(d2,columns=["Districts","Transaction amount"])
        df = df.astype({"Transaction amount":float})
        st.title(' Top 10 Districts of the year')
        st.header('with respect of transaction amount')
        fig = px.pie(df, values='Transaction amount', names='Districts')
        st.plotly_chart(fig)
     if st.sidebar.button(" Dis based on Registered_users"):
        import plotly.express as px
        query=f'''select District ,sum(Registered_users) from map_user_list where year={slideryear} group by State,
        District order by sum(Registered_users) desc limit 10 ;'''
        cur.execute(query)
        myconnection.commit()
        d2=cur.fetchall()
        df=pd.DataFrame(d2,columns=["Districts","Registered_users"])
        df = df.astype({"Registered_users":float})
        st.title(' Top 10 Districts of the year')
        st.header('with respect of Registered_users')
        fig = px.bar(df, x='Registered_users', y='Districts', orientation='h')
        fig.update_layout(xaxis_title='Registered_users', yaxis_title='Districts')
        fig.update_traces(marker_color='violet')
        st.plotly_chart(fig)
     tt=st.selectbox("types of transaction",options=["'Others'","'Financial Services'","'Merchant payments'","'Peer-to-peer payments'","'Recharge & bill payments'"])
     if st.sidebar.button(" Trend of Transaction Type"):
          import plotly.express as px
          query=f'''select Transacion_type,sum(Transacion_amount),Year from aggregate_state_transaction where Transacion_type={tt} 
           group by year ;'''
          cur.execute(query)
          myconnection.commit()
          d2=cur.fetchall()
          df=pd.DataFrame(d2,columns=["Transacion_type","Transacion_amount","Year"])
          df = df.astype({"Transacion_amount":float})
          fig = px.scatter(df, x='Year', y='Transacion_amount',text="Transacion_type")
          fig.update_traces(marker=dict(size=12, opacity=0.8, line=dict(width=2, color='DarkSlateGrey')))
          fig.update_layout(xaxis_title='Year', yaxis_title='Transacion_amount')
          st.plotly_chart(fig)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




