import random
import re
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail

from MinorProject import settings
from testapp.forms import Feedback_Data_Form, Suggestion_form
from testapp.models import Blood_Donner_Model, Feedback_Table, Suggestion_Table, Updates_Table
import requests


def sms_send(mobile):
    url = "https://www.fast2sms.com/dev/bulk"
    msg = "THis is Check msg"
    payload = "sender_id=FSTSMS&message="+msg+"&language=english&route=p&numbers="+mobile
    headers = {
        'authorization': "atT82sDKunWQjGEvN94bBrpIkzMof5Hce1xwS7LYl3VFdgRCqyoIz23OsydkUqR9ljNn8hZLM0ruKBHf",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


def home_blood(request):
    all_blood = Blood_Donner_Model.objects.all()
    all_update = Updates_Table.objects.all()
    return render(request, 'home_blood.html', {'all_blood': all_blood, 'camp_date': all_update})


def search_blood_group_view(request):
    blood_group = request.GET.get('search')
    print(blood_group, 'Group')
    blood_area = request.GET.get('area')
    blood_area = blood_area.title()
    print(blood_area, 'Area')
    if blood_group:
        matched = Blood_Donner_Model.objects.filter(Address__contains=blood_area[0])
        if matched:
            matched = Blood_Donner_Model.objects.filter(Address__istartswith=blood_area[0], Blood_Group=blood_group)
            if matched:
                return render(request, 'searched.html',
                              {'show_details': matched, 'type': 'Show_Searched'})
            no_matched = Blood_Donner_Model.objects.all()
            return render(request, 'searched.html', {'all_blood': no_matched, 'type': 'Show_Searched'})
        return render(request, 'searched.html', {'show_details': matched, 'type': 'Show_Searched'})
    elif blood_area:
        matched = Blood_Donner_Model.objects.filter(Address__istartswith=blood_area[0])
        no_matched = Blood_Donner_Model.objects.all()
        print(matched)
        return render(request, 'searched.html', {'matched': matched, 'all_blood': no_matched, 'type': 'Show_Searched'})
    else:
        no_matched = Blood_Donner_Model.objects.all()
        return render(request, 'home_blood.html', {'all_blood': no_matched})


def feedback_view(request):
    if request.method == "POST":
        form = Feedback_Data_Form(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')
            fform = Feedback_Data_Form()
            name_check = Feedback_Table.objects.filter(Feedback=feedback)
            if not name_check:
                data = Feedback_Table(
                    Name=name,
                    Rating=rating,
                    Feedback=feedback
                )
                data.save()
                form = Feedback_Data_Form()
                all = Suggestion_Table.objects.all()
                return render(request, 'feedback.html', {'feedbacks': all, 'form': form})
            form = Feedback_Data_Form()
            all = Suggestion_Table.objects.all()
            return render(request, 'feedback.html',
                          {'all': all, 'form': all, 'msg': 'Please write some unique Suggestions'})
        form = Feedback_Data_Form
        feedbacks = Feedback_Table.objects.all()
        return render(request, 'feedback.html', {'form': form, 'feedbacks': feedbacks})
    form = Feedback_Data_Form
    feed_back = Feedback_Table.objects.all()
    return render(request, 'feedback.html', {'form': form, 'feedbacks': feed_back})


def helper_view(request):
    id_no = int(request.GET.get('id_no'))
    show_details = Blood_Donner_Model.objects.filter(id=id_no)
    return render(request, 'searched.html', {'show_details': show_details, 'type': 'selected'})


def register_for_donner(request):
    if request.method == "POST":
        name = request.POST.get('f_name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        email = request.POST.get('email')
        l_b_donation = request.POST.get('l_b_donate')
        d_o_birth = request.POST.get('DOB')
        blood = request.POST.get('blood')
        if (re.findall('^[9|8|7|6]', mobile)) == "9" or '8' or '7' or "6":
            if len(mobile) >= 10:
                check = Blood_Donner_Model.objects.filter(Mobile=int(mobile))
                if not check:
                    d_o_birth_year = int(d_o_birth[0:4])
                    print(d_o_birth_year)
                    today = date.today()
                    age = today.year - d_o_birth_year
                    if age >= 17:
                        obj = EmailMessage(subject='Thanks for Registering on Blood Bank',
                                           body='please click on this link 127.0.0.1:8000/ to Veriy your email id',
                                           from_email=settings.EMAIL_HOST_USER, bcc=[email,],)
                        obj.send(fail_silently=False)
                        # Blood_Donner_Model(Mobile=mobile, Email=email, Address=address.lower(), Name=name,
                        #                    Last_Donation_Date=l_b_donation, Date_O_Birth=d_o_birth, Blood_Group=blood).save()
                        # sms_send(str(mobile))

                        matched = Blood_Donner_Model.objects.all()
                        return render(request, 'home_blood.html', {'all_blood': matched, 'type': 'saved'})
                    msg = 'Thank you for Showing Interest To Donate Blood But You are Less than 17 Years'
                    return render(request, 'registration.html', {'reply': msg})
                msg = 'This Mobile is Already Register With Other User Enter A New Number'
                return render(request, 'registration.html', {'msg': msg})
            msg = 'This Mobile is Already Register With Other User Enter A New Number'
            return render(request, 'registration.html', {'msg': msg})
        msg = 'This Mobile is Already Register With Other User Enter A New Number'
        return render(request, 'registration.html', {'msg': msg})
    return render(request, 'registration.html')


def donner_confirm(request):
    mobile = request.GET.get('mobile')
    # sms_send(str(mobile))
    all_update = Updates_Table.objects.all()
    return render(request, 'home_blood.html', {'camp_date': all_update, 'mobile': mobile, 'type': 'informed'})


def contact_us(request):
    all_blood = Blood_Donner_Model.objects.all()
    return render(request, 'contact_us.html', {'all_blood': all_blood})


def suggestions(request):
    E_form = Suggestion_form()
    if request.method == "POST":
        name = request.POST.get('name')
        suggest = request.POST.get('suggestion_name')
        name_check = Suggestion_Table.objects.filter(suggestion_name=suggest, name=name)
        if not name_check:
            Suggestion_Table(name=name, suggestion_name=suggest).save()
            all = Suggestion_Table.objects.all()
            return render(request, 'suggestions.html', {'all': all, 'form': E_form, 'name': name})
        all = Suggestion_Table.objects.all()
        return render(request, 'suggestions.html', {'all': all, 'form': E_form, 'msg': 'Please write some unique Suggestions'})
    all = Suggestion_Table.objects.all()
    return render(request, 'suggestions.html', {'all': all, 'form': E_form})


def problem(request):
    return render(request,"problem.html")


def gallery(request):
    return render(request,"gallery.html")

