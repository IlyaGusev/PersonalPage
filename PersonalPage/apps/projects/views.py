from django.views.generic import DetailView
from projects.models import Project, Category


class CategoryView(DetailView):
    template_name = "projects/category.html"
    model = Category
    context_object_name = 'category'
    slug_field = 'sname'
    slug_url_kwarg = 'category_sname'


class ProjectView(DetailView):
    model = Project
    template_name = "projects/project.html"
    context_object_name = 'project'
    slug_field = 'sname'
    slug_url_kwarg = 'project_sname'