from django.shortcuts import render
from django.templatetags.static import static
from django.templatetags.static import static



def home(request):
    # Render the home page
    hello = "Hello World!"
    return render(request,'index.html')

# # Sample static project dictionary (normally you’d use a DB)
projects_data = {
    'cart-abandonment-analysis-using-clustering': {
        'title': 'Cart Abandonment Analysis',
        'image': 'images/project1.png',
        'dashboard_html_button' : 'pdf/Analysis_cart.html',
        'dashboard_embed':  """
        <div class='tableauPlaceholder' id='viz1754300957340' style='position: relative'>
          <noscript><a href='#'>
            <img alt='Dashboard 1' src='https://public.tableau.com/static/images/Ca/Cart_17539456101170/Dashboard1/1_rss.png' style='border: none' />
          </a></noscript>
          <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='Cart_17539456101170/Dashboard1' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/Ca/Cart_17539456101170/Dashboard1/1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
            <param name='filter' value='publish=yes' />
          </object>
        </div>
        <script type='text/javascript'>
          var divElement = document.getElementById('viz1754300957340');
          var vizElement = divElement.getElementsByTagName('object')[0];
          if (divElement.offsetWidth > 800) {
            vizElement.style.width='100%'; vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
          } else if (divElement.offsetWidth > 500) {
            vizElement.style.width='100%'; vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
          } else {
            vizElement.style.width='100%'; vizElement.style.height='2127px';
          }
          var scriptElement = document.createElement('script');
          scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
          vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
        """,
        'description': 'Analyzed e-commerce behavior to identify cart abandonment patterns.',
        'details': '''
    <h3>🧩 Problem Statement</h3>
    <p>Many users add items to their carts but leave without purchasing, resulting in lost revenue. This project explores behavioral trends behind cart abandonment and identifies opportunities to improve the checkout process.</p>

    <h3>🧠 Project Approach</h3>
    <ol>
      <li><strong>Data Collection:</strong> Sourced clickstream and transaction data from the Google Merchandise Store dataset (via BigQuery).

Extracted relevant fields such as device type, traffic source, session duration, bounce rate, number of visits, and transaction revenue.

Cleaned the dataset by handling null values, converting revenue to a usable numeric format, and filtering out irrelevant sessions (e.g., bots, internal traffic).</li>
      <li><strong>Data Cleaning & Preparation:</strong> Handled missing data, timestamp parsing, session segmentation.</li>
      <li><strong>Exploratory Data Analysis:</strong> Conducted univariate and bivariate analysis to understand user behavior across different channels and devices.

Segmented users into converters (those who made purchases) and abandoners (those who didn’t).

Visualized key KPIs such as bounce rates, revenue contributions, and session durations using interactive charts..</li>
      <li><strong>User Segmentation:</strong> Grouped users based on source/medium (e.g., Google, direct, referral) to evaluate traffic quality.

Analyzed device usage (desktop vs. mobile) and its impact on abandonment rates.

Identified underperforming segments and sessions with high bounce rates but significant cart activity..</li>
      <li><strong> Visualization & Dashboarding:</strong> Created an intuitive, interactive dashboard using Tableau  to present findings.

Dashboard included: Revenue funnel, device-wise abandonment trends, traffic source effectiveness, and time-based patterns.

Enabled dynamic filtering and drill-downs for marketing teams to explore specific behaviors.</li>
    </ol>

    <h3>🛠️ Tech Stack</h3>
    <ul>
      <li>Python (Pandas, Matplotlib)</li>
      
      <li>Tableau for interactive dashboards</li>
    </ul>

    <h3>📊 Highlights</h3>
    <ul>
      <li>Performed customer segmentation and funnel analysis to classify user behavior patterns (e.g., comparison shoppers, last-minute abandoners).</li>
      <li>Conducted an in-depth behavioral analysis of over 1 million user sessions</li>
      <li>Developed a fully interactive Tableau dashboard with dynamic filters to visualize abandonment trends by channel, device type, geography, and session behavior.</li>
    </ul>
    '''
    },
    'ipl': {
        'title': 'Indian Premier League (IPL)',
        'dashboard_embed':'''<iframe title="Indian premier league(IPL)" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNGRiZjc0MTMtNmMwZS00NGIwLWI2ZWYtMTk1NjY4ZjMxMDMwIiwidCI6ImFkZDc4MGIxLWI5MzAtNGVjZS1iMjA5LTQ3ZGQ3NWEwNzhiYSJ9&pageName=a25eaa3493de7647ce3e" frameborder="0" allowFullScreen="true"></iframe>''',
        'image': 'images/project1.png',
        # 'description': 'Analyzed e-commerce behavior to identify cart abandonment patterns.',
            'details': '''
        <h3>📌 Introduction</h3>
        <p>
        An engaging IPL Interactive Dashboard packed with rich visualizations, dynamic filters, and in-depth insights — bringing player stats, team performance, and season trends to life. Dive into the data and uncover stories behind every match..
        </p>

        
        <h3>🛠️ Tech Stack</h3>
        <ul>
          <li>Power BI</li>
          <li>SQL</li>
        </ul>

        <h3>🧠 Project Approach</h3>
<ol>
  <li><strong>Data Ingestion :</strong> Sourced a data mainly from kaggle but differnt accounts or tables and stoed in SQL li>
  <li><strong>Data Cleaning:</strong> We cleaned th dataset Mainly in Sql , like i corrected the players name, team name , filled the unfilled features like dismissial etc.</li>
  <li><strong>EDA:</strong> Created a new measures and use SQl for merging the table .</li>
  <li><strong>Power BI:</strong> Created a 3 page good interactive dashboard with lot of information.</li>
</ol>





    '''
    },

    'hr-analysis': {
    'title': 'HR Analytics: Insights into Employee Attrition',
    'tools': 'PYTHON, POWER BI, PANDAS, STREAMLIT',
    'dashboard_html_button': 'pdf/HR_notebook.html',
    # 'link': "https://hr-attrition-analysis.streamlit.app/",
    'dashboard_embed': '''
        <iframe title="HR" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiZjZhYzUyOTEtMzE3Yy00Mjc1LWExNTUtMjJiMDQ0NjZiMzg3IiwidCI6ImFkZDc4MGIxLWI5MzAtNGVjZS1iMjA5LTQ3ZGQ3NWEwNzhiYSJ9" frameborder="0" allowFullScreen="true"></iframe>
         ''',
    # 'description': 'Used ML and visual analytics to understand and predict employee attrition from organizational data.',
    'details': '''
        <h3>📌 Introduction</h3>
        <p>
        Human Resources departments often struggle to understand why employees leave and how to reduce attrition. This project leverages HR analytics to derive insights from employee data and build a predictive model to flag potential attrition risks.
        </p>

        <h3>🧩 Problems</h3>
        <p>
        High attrition rates increase recruitment costs and disrupt team dynamics. The dataset includes features such as job role, age, income, work-life balance, satisfaction levels, and attrition status. The main challenge was identifying the most influential factors driving attrition and predicting it with accuracy.
        </p>

        <h3>🛠️ Tech Stack</h3>
        <ul>
          <li>Python, Pandas</li>
          <li> Scikit-learn</li>
          <li>Power BI</li>
        </ul>

        <h3>💡 Project Approach</h3>
<p>
The HR Analytics project followed a structured data science workflow, from raw data ingestion to model deployment and dashboarding. Here’s a breakdown of the step-by-step approach:
</p>

<ul>
  <li><strong>1. Data Understanding:</strong> 
    <br>We started by thoroughly analyzing the dataset which included over 30 variables related to employee demographics, job roles, compensation, work conditions, and attrition status. We conducted initial summary statistics to understand distributions, imbalance in target classes, and potential data quality issues.
  </li>

  <li><strong>2. Data Cleaning & Preprocessing:</strong> 
    <br>All categorical variables (like department, job role, marital status) were label encoded or one-hot encoded. Missing values were imputed using domain-specific logic (e.g., median imputation for numeric variables). Outliers were detected and handled through IQR filtering. Features such as 'EmployeeNumber' (irrelevant ID) were dropped.
  </li>

  <li><strong>3. Exploratory Data Analysis (EDA):</strong> 
    <br>Used correlation matrices, boxplots, and segmented bar charts to reveal key patterns. For instance, employees with low satisfaction, fewer years at company, or poor work-life balance showed significantly higher attrition rates. EDA also revealed which departments were losing the most employees.
  </li>

  <li><strong>4. Feature Engineering:</strong> 
    <br>Created new variables like <em>tenure days</em> , <em>Age</em>, and <em>tenure years</em>. These new features enhanced the predictive power and offered clearer business insights during modeling and dashboarding.
  </li>

  <li><strong>5. Model Building:</strong> 
    <br>Tested multiple clustering algorithms including k means elbow method , silhoutes scores , kmeans clustering , Agglomeartive clustering and GMM, which is critical for identify employer performance.
  </li>


  <li><strong>7. Dashboarding with Power BI:</strong> 
    <br>Created an HR dashboard showing key KPIs including attrition rate by department, average monthly income vs satisfaction score, and promotion frequency. Filters allowed HR managers to drill down by gender, job level, and age group.
  </li>



        <h3>✨ Highlights</h3>
        <ul>
          <li>Identified employer on the basis of their performance</li>
          <li><strong>Moderate Performers</strong>         1394 ,
<strong>Highly Engaged, Balanced </strong>   1133 ,
<strong>High Rated, Satisfied  </strong>    473</li>
          <li>Interactive Power BI dashboard allows HR to drill down into employees by their performance.</li>
        </ul>

        <h3>📌 Conclusion</h3>
        <p>
        The analysis offered valuable insights into employee behavior and attrition patterns. It demonstrated how data-driven HR strategies can proactively sees employees on the basis of their performance. The model and dashboard combined to deliver actionable intelligence for retention planning.
        </p>


    '''
},

   'cyclists': {
    'title': 'Cyclists Bike Usage Analytics',
    'tools': 'PYTHON, PANDAS, MATPLOTLIB, SEABORN, JUPYTER',
    'dashboard_html': static('pdf/cyclists.html'),

    # 'dashboard_html':"pdf/cyclists.html",
    
    'description': 'Analyzed how casual riders and annual members use Cyclistic bikes differently using a rich dataset of 700K+ trips.',
    'details': '''
        <h3>📌 Introduction</h3>
        <p>
        The Cyclistic bike-share program in Chicago generates massive usage data from thousands of rides daily. This project analyzes over 710,000 rides to understand how two major user types—casual riders and annual members—use the service differently. These insights aim to support business decisions for improving user engagement and retention.
        </p>

        <h3>🧩 Problem Statement</h3>
        <p>
        Cyclistic's marketing team is focused on converting more casual riders into annual members. However, without concrete behavioral insights, it's difficult to target campaigns effectively. We needed to explore usage trends to uncover what distinguishes the two groups.
        </p>

        <h3>⚙️ Tech Stack</h3>
        <ul>
          <li><strong>Python:</strong> Core language for data processing and analysis</li>
          <li><strong>Pandas & NumPy:</strong> Data wrangling and manipulation</li>
          <li><strong>Matplotlib & Seaborn:</strong> Visual exploration and presentation of patterns</li>
          <li><strong>Jupyter Notebook:</strong> Interactive coding and documentation</li>
        </ul>

        <h3>📊 Project Approach</h3>
        <ul>
          <li>Performed data cleaning (removing null stations, filtering unknowns, converting time formats).</li>
          <li>Extracted date features (hour, weekday, month) to study ride behavior temporally.</li>
          <li>Segmented analysis by user type to compare usage across start times, trip durations, and stations.</li>
          <li>Identified peak usage periods, top stations, and ride patterns for both casual and member users.</li>
        </ul>

        <h3>🌟 Highlights</h3>
        <ul>
          <li>Casual riders prefer riding on weekends and during midday hours (12 PM – 7 PM).</li>
          <li>Members ride more consistently throughout weekdays, indicating work commuting behavior.</li>
          <li>Streeter Dr & Grand Ave emerged as the top station for both groups, but casual riders over-index here.</li>
          <li>Trip duration is much higher for casual riders than for members.</li>
        </ul>

        <h3>📌 Conclusion</h3>
        <p>
        This analysis reveals clear behavioral differences: members are utility-driven (commuting), while casual users ride for leisure. These insights support strategic efforts to design membership perks that align with casual users’ habits. This project sharpened skills in EDA, user segmentation, and data storytelling.
        </p>

      
    '''
}
,

    'reliance-stock-analysis': {
    'title': 'Reliance Stock Price Analysis & Prediction',
    'tools': 'PYTHON, TABLEAU, XGBOOST, SARIMA',
     
    'dashboard_html': static('pdf/stock.html'),
    'description': 'Performed time series analysis and machine learning-based prediction on Reliance Industries’ stock prices, with interactive Tableau visualizations.',
    'details': '''
        <h3>📌 Introduction</h3>
        <p>
        Reliance Industries Limited is one of India’s largest conglomerates and a key component of the NIFTY 50 index. Understanding and predicting its stock price trends is vital for traders, analysts, and investors. 
        This project explores Reliance stock data to identify patterns, build predictive models, and present insights through interactive visual dashboards.
        </p>

        <h3>🧩 Problems</h3>
        <p>
        Stock price Analysis is inherently challenging due to market volatility, macroeconomic factors, and sudden news events. 
        Traders often rely on historical data patterns but lack a unified tool that combines statistical models, machine learning, and visual analytics for deeper insight.
        </p>

        <h3>🛠 Tech Stack</h3>
        <ul>
          <li><strong>Python</strong> – Data preprocessing, feature engineering, statistical modeling.</li>
          <li><strong>Time series</strong> 
        
        </ul>

        <h3>📈 Project Approach</h3>
        <ol>
          <li>Collected historical daily stock price data (Open, High, Low, Close, Volume).</li>
          <li>Performed Exploratory Data Analysis (EDA) – trend lines, moving averages, volatility analysis.</li>
          <li>Implemented Naïve, SARIMA, and AARIMA models .</li>
          <li>Compared models using RMSE & MAE metrics.</li>
          

        <h3>✨ Highlights</h3>
        <ul>
          <li>Compared traditional statistical and modern ML models for accuracy.</li>
          <li>SARIMA captured seasonality better</li>
          <li>Historical VaR at 95% confidence: -1.99%</li>
          <li>Parametric VaR at 95% confidence: -2.26%</li>
          
        </ul>

        <h3>📌 Conclusion</h3>
        <p>
        This project demonstrated the value of combining statistical models, ML algorithms, and visual analytics for financial forecasting. 
        AARIMA and SARIMA provided complementary strengths, and . 
        This strengthened my skills in time series modeling, ML workflow.
        </p>
    '''
},

    'delhi-rent-prediction': {
    'title': 'Delhi Rent Price Analysis & Prediction',
    'tools': 'PYTHON, POWER BI, STREAMLIT', 
    'dashboard_html_button': 'pdf/Delhi_Rent_insights.html',
    'link': "https://delhi-rent-predictor.streamlit.app/",
    'dashboard_embed': '''
        <iframe title="Delhi Rent Report" width="100%" height="400" 
        src="https://app.powerbi.com/view?r=eyJrIjoiZGY5MzM3MmUtMWNkOS00ZGVhLTlmMDAtNzdkM2I0OTdmMTZjIiwidCI6ImFkZDc4MGIxLWI5MzAtNGVjZS1iMjA5LTQ3ZGQ3NWEwNzhiYSJ9" 
        frameborder="0" allowFullScreen="true"></iframe>
    ''',
    'description': '',
    'details': '''
        <h3>📌 Introduction</h3>
        <p>
        Delhi’s rental housing market is complex, with huge variations based on locality, amenities, and property size. Tenants often face difficulty finding fair prices while landlords lack data to price competitively. This project simulates a real-world rent prediction scenario where insights and predictions help both parties. The project assumes rent is mainly influenced by locality, square foot , and number of bedrooms in house.
        </p>

        <h3>🧩 Problems</h3>
        <p>
        The rental pricing lacks transparency and standardization. We analyzed a dataset containing house features like area, BHK, location, and price. Using correlation analysis, visualizations, and feature importance (via RandomForest), we identified locality and size as most influential features. 
        </p>

        <h3>🛠️ Tech Stack</h3>
        <ul>
          <li>Python, Pandas, Scikit-learn</li>
          <li>Streamlit</li>
          <li>Power BI</li>
        </ul>

        <h3>🧠 Project Approach</h3>
<ol>
  <li><strong>Data Ingestion :</strong> Sourced real estate data of Delhi from Kaggle and Delhi govt. sites and stored in SQL database.</li>
  <li><strong>Data Cleaning:</strong> Handling Missing values , Find the Duplicate And Outliers , Correct the Errored Features Like locality & Suburban name .</li>
  <li><strong>EDA:</strong> The EDA process began with a thorough examination of the dataset, checking for missing values, duplicates, and inconsistencies. Key variables like location, BHK, bathrooms, and total area were analyzed to understand their impact on house prices. We used distribution plots, boxplots, and heatmaps to identify outliers, skewed data, and correlations. The location feature was found to be highly cardinal, so it was cleaned and grouped for better analysis. Price trends across locations and BHK combinations revealed important market patterns, forming the foundation for feature engineering. This data-driven understanding shaped the preprocessing and modeling steps ahead.</li>
  <li><strong>Model Building:</strong> Trained regressors (Linear, Random Forest, Gradient Boosting). Selected best model with GridSearchCV.</li>
  <li><strong>Prediction Interface:</strong> Streamlit app with user input and Power BI visuals.</li>
</ol>



<h3>📊 Highlights</h3>
<ul>
  <li>R² > 0.82 on test set</li>
  <li>Interactive BI dashboard</li>
  <li>Deployed rent prediction app</li>
</ul>



        <h3>📌 Conclusion</h3>
        <p>
        The ML-based prediction solution using Random Forest gave an R² of 0.82+, demonstrating reliable performance. Visual analysis with Power BI also revealed clusters of high-rent and low-rent zones.
        </p>

    '''
},

'resume-screening': {
    'title': 'Smart Resume Screening Engine',
    'tools': 'SQL, PostgreSQL, NLP, Python, Pandas, Streamlit',
    'dashboard_html': static('pdf/Resume_analysis.html'),

    'description': 'Built a SQL + NLP-powered engine to automatically match candidate resumes with job requirements based on skill overlap and experience levels.',
    'details': '''

                   <h3>📷 Project Screenshot</h3>
            <img src="{img_url}" 
                 alt="Resume Screening Engine Screenshot"
                 style="width:100%; max-width:600px;  border-radius:8px; margin:10px 0;">

    
        <h3>📌 Introduction</h3>
        <p>
        The hiring process often involves screening hundreds of resumes for a single job opening, which can be slow and subjective. This project aims to automate and optimize resume screening using a combination of structured SQL queries and unstructured text analysis (NLP). By matching candidates to jobs based on skills and experience, it significantly reduces recruiter effort and improves the fairness of shortlisting.
        </p>

        <h3>🧩 Problem Statement</h3>
        <p>
        HR teams waste hours manually scanning resumes, and relevant candidates often get overlooked due to inconsistency in screening. The challenge was to build a scalable system that could parse resumes, store structured information in a relational database, and return ranked matches for each job posting.
        </p>

        <h3>⚙️ Tech Stack</h3>
        <ul>
          <li><strong>PostgreSQL:</strong> Storing job, resume, and skill data with relationships for efficient querying</li>
          
          <li><strong>Python (Pandas, Regex, SpaCy):</strong> Parsing resumes to extract skills and experiences</li>
          
        </ul>

        <h3>📊 Project Approach</h3>
        <ul>
          <li>Designed an ER model with <code>jobs</code>, <code>job_skills</code>, <code>resume_details</code>, and <code>resume_skills</code> tables.</li>
          <li>Extracted skills and experience from resumes using Python + NLP.</li>
          <li>Loaded parsed data into PostgreSQL for structured querying.</li>
          <li>Created SQL queries to rank candidates by skill match count and experience fit.</li>
          <li>Developed a Streamlit interface to display ranked candidates per job role.</li>
        </ul>

        <h3>🌟 Highlights</h3>
        <ul>
          <li>Implemented a skill matching algorithm using SQL joins and COUNT aggregation.</li>
          <li>Ranked candidates by both skill match percentage and years of experience.</li>
          <li>Added analytics views for in-demand skills and top-matched candidates.</li>
          <li>Produced an ER diagram for database schema documentation.</li>
        </ul>

        <h3>📌 Conclusion</h3>
        <p>
        This project demonstrates how SQL and NLP can work together to solve real-world recruitment problems. By automating candidate-job matching, HR teams can make faster, data-driven decisions, reduce bias, and focus on high-value interviewing. The project strengthened skills in relational database design, advanced SQL querying, and natural language text processing.
        </p>
    '''
}

}
def project_detail(request, slug):
    project = projects_data.get(slug)
    if not project:
        return render(request, '404.html', status=404)
    return render(request, 'project_detail.html', project)

def project_list(request):
    return render(request, 'index.html')

