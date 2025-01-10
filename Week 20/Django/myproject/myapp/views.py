from django.shortcuts import render
from django.http import HttpResponse
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import base64
import pandas as pd
# Create your views here.
def bar_chart_view(request):
    # Data for the bar chart
    data = {
        "Category": ["A", "B", "C", "D"],
        "Values": [23, 45, 56, 78]
    }

    # Create the plot
    df = pd.DataFrame(data)
    matplotlib.use('Agg')
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 6))
    # plt.subplot(2,2,1)
    bar_plot = sns.barplot(x="Category", y="Values", data=df)
    bar_plot.set_title("Live Bar Chart Example", fontsize=16)
    bar_plot.set_xlabel("Category", fontsize=12)
    bar_plot.set_ylabel("Values", fontsize=12)
    # plt.subplot(2,2,2)
    # bar_plot = sns.scatterplot(x="Category", y="Values", data=df)
    # bar_plot.set_title("Live Bar Chart Example", fontsize=16)
    # bar_plot.set_xlabel("Category", fontsize=12)
    # bar_plot.set_ylabel("Values", fontsize=12)

    # Convert plot to base64
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()
    plt.close()

    # Pass the base64 image string to the template
    return render(request,'index.html',{'plot':img_base64})