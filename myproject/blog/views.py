
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import models
from . import forms


# Create your views here.
def index(request):
	posts = models.Post.objects.all()
	return render(request, 'blog/index.html', {'posts':posts})


def detail(request, pk):
	post = get_object_or_404(models.Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})



def comment_new(request, pk):
	post = get_object_or_404(models.Post, pk=pk)
	form = forms.CommentForm()
	if request.method == 'POST':
		form = forms.CommentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(post.get_absolute_url())
	return render(request, 'blog/post_form.html', {'form':form})		


def comment_edit(request, post_pk, pk):
	post = get_object_or_404(models.Post, pk=post_pk)
	comment = get_object_or_404(models.Comment, pk=pk)
	form = forms.CommentForm(instance=comment)
	if request.method == 'POST':
		form = forms.CommentForm(instance=comment, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(post.get_absolute_url())
	return render(request, 'blog/post_form.html', {'form':form})


def post_new(request):
	if request.method == 'POST':
		pass
	return render(request, 'blog/post_form.html')
