---
layout: post
title: "Greed... Is Good - A Tale of GitHub Pages Migration"
author: "Xiaofeng"
tags: [Tech]
---

In the great movie [Wall Street (1987)](https://www.imdb.com/title/tt0094291/), Mr. Gekko said the following famous quote: 

> Greed, for lack of a better word, is good.

Since I went with GoDaddy instead of Namecheap to get this domain, it'd be a crime to pay another dime for hosting eh? Luckily, nowadays there're free and decent hosting services available, from vendors like GitHub and GitLab. Out of complete 100% objectivity (has nothing to do with me currently working for Microsoft), I decided to try on GitHub Pages. :)  

I jotted down some basic steps for this migration, and I have to say, it's pretty neat. 

## Create Your GitHub Pages Site 

It's pretty well [documented](https://docs.github.com/en/github/working-with-github-pages/creating-a-github-pages-site) on GitHub. Very painless setup, make sure that your site repo name matches your username. 

After your repo is set up, clone to your local computer for further devs. 

## Build and Polish Your Site 

Again, `Greed is Good` here, no need to build everything from the scratch, just pick a reputable static site generator. I went with [Jekyll](https://jekyllrb.com/) with [Tale](https://github.com/chesterhow/tale) theme. But there're lots of other fish in the sea.
 
I did this on a Macbook Pro, for some reasons, the system default ruby version was too low, so I had to upgrade it: 

```
brew install chruby ruby-install
ruby-install ruby 2.7
source /usr/local/opt/chruby/share/chruby/chruby.sh
source /usr/local/opt/chruby/share/chruby/auto.sh
chruby 2.7.2 
```

I was very pleased with the rich markdown support by Jekyll. You can edit the posts with your favorite markdown editor. As a lazy man, I simply typed in vim in my local terminal. 

## Deploy Your Site 

GitHub Pages has continuous integration (CI) and delopyment (CD) now. All your have to do is configuring which branch triggers it. Deployment, aka publishing, is as simple as a `git push`. But be a pro, set up a local `dev` branch for drafts and experimental features. Maybe even a `hotfix` branch to hotfix things if you want to be hardcore! 

## Add Custom Domain on GitHub Pages 

This is the final piece of the puzzle, and it can be a bit tricky. 

There's a great read by GitHub [docs](https://docs.github.com/en/github/working-with-github-pages/about-custom-domains-and-github-pages), but alternatively, you can just get away with adding a `CNAME` file in your aforementioned site repo, with nothing but your domain, e.g. example.com, in the file. Push it to GitHub and wait for it to take effect. 

Now, you want to go to your domain provider's admin page, and play with the DNS settings as specified in same doc link in last paragraph. For me, since I used GoDaddy, it doesn't seem `CNAME @` addition was allowed, so I ping'ed github.io and added the IP to `A @` record. Let's hope that IP won't be changed by GitHub soon. 

## But, But, What About HTTPS? 

It's hard to get around without HTTPS nowadays. But worry not, GitHub has our back on this too! That is, if you pleased them with your **correct** DNS settings. You can enforce HTTPS traffic to your site by toggling on your site repo (yourname.github.io) setting's `enforce HTTPS` - note that it could take up to 24 hours before the https certs are properly generated upon your correct DNS setup. 


## Conclusion 

Back in the good old days, all these fancy HTTPS, hosting and site management, aint that intuitive, or.. free for that matter. So I'm truly impressed with this smooth GitHub Pages migration exprience, and of course, their generosity. I can maybe splurge the $$$ saved on hosting on some other things. :D 

When it comes to build a site, I'd agree with Mr. Gekko here: there's nothing to be ashamed to be a greedy cheapskate - go nuts with the free resources. Big thanks to the hardwork of open source community contributors; they're truly the lynchpin of our modern society! 

And.., a little patience goes a long way too. When you're tweaking stuff, you're bound to be frustrated with minor hiccups here and there. But Google is your friend. :)
