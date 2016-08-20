# leetcode-cli

[![npm version](https://img.shields.io/npm/v/leetcode-cli.svg?style=flat)](https://www.npmjs.com/package/leetcode-cli)
[![license](https://img.shields.io/npm/l/leetcode-cli.svg?style=flat)](https://github.com/skygragon/leetcode-cli/blob/master/LICENSE)

A cli tool to enjoy leetcode!

Great thanks to leetcode.com, an really awesome website!

## Table of Contents

* [Install](#install)
* [Quick Start](#quick-start)
	* [Login](#1-login)
	* [List](#2-list)
	* [Prepare](#3-prepare)
	* [Coding](#4-coding)
	* [Test](#5-test)
	* [Submit](#6-submit)

## Install

    $ sudo npm install -g leetcode-cli

## Quick Start

### 1. Login

Login with your leetcode account (username or email).

	$ lc user -l
	login: <account>
	pass:
	Successfully login as <account>

* `-l` to login
* `-L` to logout.
* `lc user` to show current account.

### 2. List

Navigate all the problems. The heading `✔` means you have AC-ed the problem.

    $ lc list

      [385] Mini Parser                                                  Medium (26.5%)
    ✘ [384] Shuffle an Array                                             Medium (45.7%)
    ✔ [383] Ransom Note                                                  Easy   (44.5%)
    ✔ [382] Linked List Random Node                                      Medium (46.6%)
    ......
    ✔ [  4] Median of Two Sorted Arrays                                  Hard   (19.6%)
    ✔ [  3] Longest Substring Without Repeating Characters               Medium (22.9%)
    ✔ [  2] Add Two Numbers                                              Medium (24.5%)
    ✔ [  1] Two Sum                                                      Easy   (25.6%)

* `-D` to only show undone problems.

### 3. Prepare

Select one problem to fight. With `-g`+`-l`, the code template could be auto generated for you.

    $ lc show 1 -g -l cpp

    [1] Two Sum    	(File: two-sum.cpp)

    https://leetcode.com/problems/two-sum/

    * Easy (25.6%)
    * Total Accepted: 274880
    * Total Submissions: 1074257

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution.

    Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

    UPDATE (2016/2/13):
    The return format had been changed to zero-based indices. Please read the above updated description carefully.

* `-g` to generate source file.
* `-l` to choose programming language. (Depends on which langs are provided on leetcode)
	* c
	* cpp
	* csharp
	* golang
	* java
	* javascript
	* python
	* ruby
	* swift
* Instead of index, you can use name to select one problem.
	* `lc show "Two Sum"`
	* `lc show two-sum`

### 4. Coding

No trick, it's all your showtime!

### 5. Test

Customize your testcase and run it against leetcode.

	$ lc test ./two-sum.cpp -t '[3,2,4]\n7'

	Input data:
	[3,2,4]
	7

	Your
		✔ runtime: 0 ms
		✘ answer: [1,2]
		✔ output:

	Expected
		✔ runtime: 0 ms
		✔ answer: [0,2]
		✔ output:

* `-t` to provide test case in command line.
* `-i` to provide test case in interactive mode.

### 6. Submit

	$ lc submit ./two-sum.cpp
		✔ Accepted
		✔ 16/16 cases passed (12 ms)
