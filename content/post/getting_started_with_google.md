---
title: "Initial site improvements using Google's tools"
date: 2022-06-28T08:21:02+03:00
tags: 
- hugo
- cloudflare
- google
---

I recently had my second experience of publishing a website. This time, it was for my wife's clinic. Like this blog, I used [hugo](https://gohugo.io/). Unlike this blog, I used [cloudflare pages](https://pages.cloudflare.com/) for the hosting. In this blog post, I'll describe my initial steps improving the website with Google's tools. 

## Google Analytics

I'm definitely not an expert of using Google Analytics, but I did know from the beginning that I would like to get basic analytics of my wife's site. I've had a good experience with Google Analytics with this blog, and hugo has built-in support for it - so I added that. For that, I had to [add support for the template generation](https://github.com/bugok/hugo-html5up-alpha/commit/2ca8d9101f293ca711551d70984c90270e4541c0), and create a Google Analytics property. 

Turns out that there are multiple types of Google Analytics properties. I've found [this](https://support.google.com/analytics/answer/11986666?hl=en#zippy=%2Cin-this-article) which compares Google Analytics 4 vs. Google Analytics Universal which says: 

> Universal Analytics highlights Total Users (shown as Users) in most reports, whereas GA4 focuses on Active Users (also shown as Users). So, while the term Users appears the same, the calculation for this metric is different between UA and GA4 since UA is using Total Users and GA4 is using Active Users. 

At some point, with this blog, I got a warning prompt to move from the universal version to the 4 version. I just wanted the warning to go away so I moved to the 4. With my wife's website, I used the Google Analytics 4 right off the bat. Creating it was a bit cumbersome, but after a few clicks I had a property I could use: 

![](/google_analytics_1.png)
![](/google_analytics_2.png)

## Getting the website to show up in Google Search

The expected audience for my wife's website are people who explicitly search for her name using Google. Therefore, I wanted to make sure that the website shows up in Google's index. 

A few days after I published the website - it still didn't show up in Google's search results. I wanted to fix that.

To do that, I remembered a post somewhere which talked about [Google Search Console](https://search.google.com/search-console/), where you could ask Google to crawl your website. 

### Authentication to Google Search Console using DNS

When using Google Search console for your website, you first need to prove that you own the website. This is done by adding a TXT DNS record with a generated value to the root domain. In my case, since I'm using cloudflare for the domain, it was simple: 

![](/cloudflare_dns_txt.png)

A few moments later, I was able to get started with Google Search Console

### Error: Crawled - Currently Not In Indexed

When instructing Google Search Console to parse the website's `sitemap.xml` - I got this error: `Crawled - Currently Not In Indexed`. The webpage seemed fine - I couldn't figure out why this was erroring out. 

Eventually, I looked at the raw `sitemap.xml`:

```lang=xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
	<url>
		<loc>/</loc>
		<lastmod>2022-04-08T23:27:51+03:00</lastmod>
	</url>
	<url>
		<loc>/about/</loc>
	</url>
	<url>
		<loc>/treatment/</loc>
	</url>
	<url>
		<loc>/contact/</loc>
	</url>
</urlset>
```

I thought that since I was using hugo's `baseURL` to be `/`, the generated `sitemap.xml` wasn't parsed well. I changed the `baseURL` in the config, deployed the website - and the `sitemap.xml` now had the base domain: `https://mywebsite.com/` as the prefix. Google Search Console was happy about the `sitemap.xml`. 
A few days later, the website started to show up in Google's search result. 

## How performant is my website? Enter PageSpeed.

I believe I loaded and reloaded the website tens or hundreds of times. But, I wanted to get a more objective and quantitive numbers about the site's performance. I found [Google's PageSpeed Insights](https://pagespeed.web.dev/). A few click, and I was able to see that the site's performance is good enough (given that I haven't invested anything in making it performant). 

The mobile site is OK: 

![](/pagespeed_mobile.png)

The desktop site is really good: 

![](/pagespeed_desktop.png)

## What's next? 

I've added a favicon :)
Other than that, I guess there will be small improvements over time.

