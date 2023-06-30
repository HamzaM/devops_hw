from django.shortcuts import render
from django.http import HttpResponse
from kubernetes import client, config

def index(request):
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    pod_list = v1.list_namespaced_pod(namespace='default')
    return HttpResponse(pod_list)