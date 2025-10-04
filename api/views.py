"""
API views for Cookie-Licking Detection system
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import JsonResponse

from .models import GitHubUser, ContributorProfile, Issue, Repository
from .serializers import (
    GitHubUserSerializer, ContributorProfileSerializer, 
    IssueSerializer, RepositorySerializer
)


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """Health check endpoint"""
    return Response({
        'status': 'healthy',
        'message': 'Cookie-Licking Detection API is running',
        'version': '2.0'
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def api_info(request):
    """API information endpoint"""
    return Response({
        'name': 'Cookie-Licking Detection API',
        'description': 'AI-powered system to detect and resolve issue assignment abandonment',
        'features': [
            'GitHub OAuth integration',
            'AI-powered trust scoring',
            'Automated reminder system',
            'Smart contributor analysis'
        ],
        'endpoints': {
            'health': '/api/health/',
            'info': '/api/info/',
            'github_auth': '/api/auth/github/login/',
            'issues': '/api/issues/',
            'contributors': '/api/contributors/'
        }
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def list_contributors(request):
    """List all contributor profiles"""
    contributors = ContributorProfile.objects.all().order_by('-trust_score')[:10]
    serializer = ContributorProfileSerializer(contributors, many=True)
    return Response({
        'contributors': serializer.data,
        'total_count': ContributorProfile.objects.count()
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def list_issues(request):
    """List all issues"""
    issues = Issue.objects.filter(state='open').order_by('-created_at')[:20]
    serializer = IssueSerializer(issues, many=True)
    return Response({
        'issues': serializer.data,
        'total_count': Issue.objects.filter(state='open').count()
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def stats(request):
    """Basic statistics"""
    return Response({
        'total_contributors': ContributorProfile.objects.count(),
        'total_issues': Issue.objects.count(),
        'open_issues': Issue.objects.filter(state='open').count(),
        'assigned_issues': Issue.objects.exclude(assignee__isnull=True).exclude(assignee='').count(),
        'repositories': Repository.objects.count(),
        'github_users': GitHubUser.objects.count()
    })
