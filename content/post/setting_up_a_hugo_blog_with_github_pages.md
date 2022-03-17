---
title: "Setting up a blog using Hugo and Github pages"
date: 2022-02-25T21:43:08+02:00
tags: 
- "hugo"
---

In this first post, in an inception-like manner, I'll share how I got this blog to work. 

## Starting point

This started with a Facebook group post which asked what is a good platform to host a blog. There were a few answers, but the hugo and github pages caught my eye, so I thought I'll give it a go. 

I Googled a bit and found [this guide](https://levelup.gitconnected.com/build-a-personal-website-with-github-pages-and-hugo-6c68592204c7). That was a good starting point, as it allowed me to get something to work - but I wasn't fully happy with the end result. 

## Improving the publishing flow

[Hugo](https://gohugo.io/) is a framework for building websites. You install a CLI (`hugo`), you create a site template, pick a theme, add some content, run a build command which generates files - and there you have your static content you can publish. The guide was simplifying the publishing part by suggesting to **manually add the generated files** to source control, using the structure needed by github pages. 

I wanted to have **everything** in source control - not only the generated files. For that, I needed to find a good way to do the publishing part. Meaning, how to publish the blog when a new commit is pushed. 

The answer for that - Github Actions. 

I'll describe how I got from nothing - to full deployment (including debugging some issues).


## Running the website locally

Install hugo:

```lang=bash
brew install hugo
```

Create the hugo template
```
$ cd ~/sources/
$ hugo new site blog 
```

Here is where I eventually decided to diverge form that guide. I needed to pick a theme for my site. https://themes.gohugo.io/ is a good place for this. After I picked [Binario](https://binario.netlify.app/), I then made the mistake of cloning the repository inside of `~/sources/blog/themes`. What I should have done (and eventually did) was to add it as a git submodule: 

```
$ cd ~/sources/blog
$ git init  # Initialize the repo
$ git remote add origin git@github.com:bugok/blog.git
$ git submodule add https://github.com/vimux/binario themes/binario
```

At this point, the local directory is ready to handle new content:
```
hugo new about.md
```

It took me some time to realize that the template I was using expects the content to be under `blog/content/post` and not under `blog/content/` which is where the `hugo new about.md` command created the file.

I then opened the file in an editor, made some changes, and ran the build command: 
```
hugo
```

Finally, for local debugging, you can start a local hugo server which can serve your website locally: 
```
hugo server -D
```

The `-D` part is to track draft content (this is the default when new content is generated).

And there is was: 

![About](/about_local.png)

The first dummy post was successfully loaded!


## Pushing to github

Running a website on the laptops is cool, but I wanted to share it with the rest of the world. Running the following pushed the code to github:

```
$ git add .
$ git push origin master
```

However, this isn't good enough, as this isn't the format that github pages is expecting. Here's where Github Actions come into play. [This link](https://gohugo.io/hosting-and-deployment/hosting-on-github/) shares a drop-in configuration for the `.github/workflows/gh-pages.yml` file you can add to your repo and will configure the needed actions to publish to github pages. 

As mentioned in the link, I had to change the source branch to `gh-pages`. See here: 

![Github Branch](/github_branch.png)

Also, I needed to change the default branch to `main` instead of `master`.

## Debugging images not showing

When working against a local hugo server I noticed that images weren't showing up properly. For example: 

![Image not showing](/image_not_showing.png)

Googling this, I found many references on how the simplest way to make it work is to save images under the `static` folder of the hugo directory. Upon build, all files under `static` show up at the root of the website. It should have worked, but it didn't. 

Eventually what helped was to open up Chrome Developer Tools and see the following: 

![](/static_path.png)

Turns out that this didn't work since I'm not using the website's root, but to the `/blog` path. Changing `![About](/about_local.png)` to `![About](/blog/about_local.png)` fixed the issue.

## Edit

Since writing this post - I've been trying to move everything to a custom domain - which made me drop the `/blog` path. Which means I'm not using that anymore, but using the / path.

## References

- [Hugo's quick start guide](https://gohugo.io/getting-started/quick-start/)
- [Using Github Actions to publish to Github Pages](https://gohugo.io/hosting-and-deployment/hosting-on-github/)
