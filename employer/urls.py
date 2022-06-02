from django.urls import path
from employer import views
urlpatterns=[
  path('home',views.EmployerHomeview.as_view(),name="emp.home"),
  path('jobs/add',views.AddJobView.as_view(),name="emp-addjob"),
  path("jobs/all",views.ListJobView.as_view(),name="emp-alljobs"),
  path("jobs/details/<int:id>",views.JobDetailsView.as_view(),name="emp-jobdetails"),
  path("jobs/edit/<int:id>",views.JobEditView.as_view(),name="emp-jobedit"),
  path("jobs/remove/<int:id>",views.JobDeleteView.as_view(),name="emp-jobdelete"),
  path("users/accounts/signup",views.SignUpView.as_view(),name="signup"),
  path("users/accounts/signin",views.SignInview.as_view(),name="signin"),
  path("users/accounts/signout",views.signout_view,name="signout"),
  path("users/accounts/passwordchange",views.ChangePasswordView.as_view(),name="change-password"),
  path("users/accounts/passwordreset",views.PasswordResetView.as_view(),name="reset-password")
  
]