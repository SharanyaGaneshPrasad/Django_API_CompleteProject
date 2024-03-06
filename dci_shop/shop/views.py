from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def products(request):
    response= requests.get("http://127.0.0.1:8000/products/")
    products=response.json()
    page1=f"""
    <!DOCTYPE html>
    <html>
    <body>
    
        <h1>DCI Shop!</h1>
        <h1>DCI Productslist!</h1>
    """
    for i in products:
        page1+="<li>"+i["product_name"]+ "-" + str(i["quantity"])+ "</li>"
        

    page2=f"""           
    </body>
    </html>
    """
    return HttpResponse(page1+page2)


def users(request):
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    users=response.json()
    page1=f"""
    <!DOCTYPE html>
    <html>
    <body>
    
        <h1>DCI Shop!</h1>
        <h1>DCI Userslist!</h1>
    """
    for i in users:
        page1+="<li>"+i["name"]+ "  -  " + str(i["phone"])+ "  -  "+ i["email"]+"</li>"
        

    page2=f"""           
    </body>
    </html>
    """
    return HttpResponse(page1+page2)