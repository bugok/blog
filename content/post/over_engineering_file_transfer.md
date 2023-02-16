---
title: "Over engineering file transfer"
date: 2022-04-01T14:11:00+03:00
tags: 
- overengineering
- usb
- ftp
- smb
summary: When you can't use your mass storage device as is, you can over-engineer the network to transfer files.
description: When you can't use your mass storage device as is, you can over-engineer the network to transfer files.
---

## Context

On Thursdays, I take my younger daughter to a swimming lessons. Sometimes, I take my GoPro with me. I take a video during the lesson and when I get home I edit the video, upload and share it with friends and family. In the last few days, I realized that I may not be able to connect mass storage devices to my laptop, so I tried to find another solution to transfer the files from my GoPro to my laptop. 

This was over-engineering the solution, but I did learn a few things along the way. 

## USB over the network

The direction I wanted to take was to stick the micro SD card into two adapters (`microSD` -> `SD` -> `USB A`), connect that to another device and make that USB device available over the network.

![](/sd_adapters.jpeg)

## First, Windows

I have a laptop at home, which runs Windows. My initial thought was to connect the adapters to the Windows laptop, share that directory from the Windows laptop and connect to that shared directory from my MacOS laptop. After about 15 minutes of tinkering and reading online tutorials - I gave up. I wasn't able to connect to the Windows machine.

## Nearby router

One of the reasons I gave up on the Windows laptop is because I remembered that the router my laptop is connected to has a USB port. I then thought that I could connect the adapters to the router and somehow get to the content over the network. I have an old [TP Link TL-WDR3600](https://www.tp-link.com/us/home-networking/wifi-router/tl-wdr3600/) which has two USB ports.

![](/tp_link_n600.jpeg)

I connected the adapters to the USB port, the LED turned on - but the router didn't recognize it. Obviously, the solution was to turn it on and off. I disconnected and reconnected the adapters, and nothing. Tried the second USB port: LED turned on - but still, nothing showed up in the router: 

![](/tplink_no_usb.png)

Why? Google again, get to [this FAQ](https://www.tp-link.com/us/support/faq/2289/). Turns out that some (old) TP-Link routers support only FAT/FAT32/NTFS file system formats. I had a hunch that it's related, so on the Windows laptop - I checked the microSD filesystem - and there is was: exFAT. 

From [this link](https://havecamerawilltravel.com/gopro/sd-card-gopro-hero7), I found that: 

> microSDHC cards use FAT32; microSDXC cards use exFAT

Also, it says: 

> But there is one aspect where you will see a big difference: microSDHC cards are 32GB or smaller while microSDXC cards are 64GB or larger.

As you can see in the previous image, my microSD card is 64GB, so it made sense. 

## Main router

A few months ago, I upgraded my main router to a [TP-Link Archer AX-20](https://www.tp-link.com/us/home-networking/wifi-router/archer-ax20/). I figured that since it's relatively new, it'll support exFAT, and it does! 

I plugged in the adapters, and I was able to see that it was recognized in the web UI.

## FTP vs. SMB

From the TP-Link web UI:

![](/tp_link_ftp_samba.png)

> Samba for Windows

Then I shouldn't use samba, right? I started with accessing the file using FTP. I started copying the first 3GB file, but after a few minutes the copying errored out because of some cryptic error. Then, I moved to samba (Finder -> Go -> Connect to server -> add `smb://192.168.0.1`), and I was able to copy the files quicker and without errors.

## Going forward

Next time, I know I will be able to connect the microSD with the adapters directly to the main router, but that will require opening the shoe closet, and it's a bit inconvenient. I did think about the option of upgrading my close router to a newer version, but the [TP-Link Archer AX-10](https://www.tp-link.com/us/home-networking/wifi-router/archer-ax10/) doesn't have a USB port, and getting another AX-20 seems like an overkill (plus, my wife vetoed against me getting another router. I can see where she's coming from). 

So, looks like I'm going to use the main router for this going forward.

Circling back to my original goal - here's the [swimming lesson video](https://www.youtube.com/watch?v=wbvn2UjgUmM) which I was eventually able to create.
