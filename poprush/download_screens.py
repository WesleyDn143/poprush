import urllib.request
import os

urls = {
    "index.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzQ0MTg0N2JhOTQ3ODRlOWJiZDA1YzM4NTk1M2Q1OTExEgsSBxDr-dLGwQ8YAZIBJAoKcHJvamVjdF9pZBIWQhQxNTQwMDk3ODI0NjAzMzUwNTQxMw&filename=&opi=89354086",
    "flavors.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzhkMzY3ZjE3ZGY0ZTQxMDRiYjY5ZDNkZmZjOTg2YjQ0EgsSBxDr-dLGwQ8YAZIBJAoKcHJvamVjdF9pZBIWQhQxNTQwMDk3ODI0NjAzMzUwNTQxMw&filename=&opi=89354086",
    "bulk.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzhiMmVlY2YyZjJkMTRjMGFhNGI3OTRiNTdkZjg1NmE2EgsSBxDr-dLGwQ8YAZIBJAoKcHJvamVjdF9pZBIWQhQxNTQwMDk3ODI0NjAzMzUwNTQxMw&filename=&opi=89354086",
    "contact.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2I3NDlkYTNjMDg5NDQ0NDI5ZGI3NWQyMWIzMTk5MDIxEgsSBxDr-dLGwQ8YAZIBJAoKcHJvamVjdF9pZBIWQhQxNTQwMDk3ODI0NjAzMzUwNTQxMw&filename=&opi=89354086",
    "order.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzM2MjExMTUxNjcxYzQwYzlhZjRhZmQ4NGRmYWE3ODEyEgsSBxDr-dLGwQ8YAZIBJAoKcHJvamVjdF9pZBIWQhQxNTQwMDk3ODI0NjAzMzUwNTQxMw&filename=&opi=89354086"
}

for filename, url in urls.items():
    try:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
