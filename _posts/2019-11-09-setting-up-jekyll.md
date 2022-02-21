---
layout: post
title: Setting up Jekyll
---

Recently was able to experience the joy of setting up Jekyll and Github Pages in more detail through setting up an internal documentation hub at work.

[Setting up Jekyll](https://jekyllrb.com/docs/)

What is Jekyll (to me). A system to automatically construct a website from
simple markdown and structured data in the form of yaml that is ligh weight
but very flexible.

A Friendly Template
-------------------

An extremely helpful starting point is the [template](https://github.com/kbroman/simple_site) provided by [Karl Broman](https://kbroman.org/pages/about.html). With great instructions on how to get started
with Jekyll and Github Pages.

Ruby Update
-------------

Mac OSX default Ruby was many version behind what was needed for Jekyll. As of (2019-11-08) Current stable version of Ruby is `2.6.5`.

I have not had much experience with [Ruby[(https://en.wikipedia.org/wiki/Ruby_(programming_language)) - but a quick read makes it sound delightful, and I am interested in how to relate the design principles 
to a mathemtical theory of the cost of surprise / complexity in a code base.

Updating and setting the new version as the default.

```
curl -L https://get.rvm.io | bash -s stable
rvm install ruby-2.6.3
rvm --default use 2.6.3
```

Jekyll Setup
------------

```
gem install jekyll bundler
cd <path_to_jekyll_data>
bundle install
```
Serving jekyll pages

```
bundle exec jekyll serve
```

For `bundle install` I was missing a `source` in the Gemfile.
Following the helpful error message to add`source 'https://rubygems.org'` resolved instantly.

