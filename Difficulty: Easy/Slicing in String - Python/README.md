<h2><a href="https://www.geeksforgeeks.org/problems/slicing-in-string-python/1?page=1&category=python&sortBy=submissions">Slicing in String - Python</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="user-select: auto;"><p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Here we'll talk about the novel and perhaps tantalizing concept of <strong style="user-select: auto;">slicing</strong>. Slicing is the process through which you can extract some continuous part of a string. For example: string is "<strong style="user-select: auto;">python</strong>", let's use slicing in this. Slicing can be done as:</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">a.</strong> string<strong style="user-select: auto;">[0:2]</strong> = <strong style="user-select: auto;">py</strong> (Slicing till index 1)<br style="user-select: auto;">
<strong style="user-select: auto;">b.</strong> string<strong style="user-select: auto;">[0:]</strong> = <strong style="user-select: auto;">python</strong> (Slicing till last index)<br style="user-select: auto;">
<strong style="user-select: auto;">c.</strong> string<strong style="user-select: auto;">[0:4]</strong> = <strong style="user-select: auto;">pyth</strong> (Slicing till index 3)<br style="user-select: auto;">
<strong style="user-select: auto;">d.</strong> string<strong style="user-select: auto;">[0:-2]</strong> = <strong style="user-select: auto;">pyth</strong> (Slicing till index -3).<br style="user-select: auto;">
<strong style="user-select: auto;">Note:</strong> <strong style="user-select: auto;">-1</strong> indexing starts from last of any string.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;">Now, lets look into this through a question. Given a string of braces named <strong style="user-select: auto;">bound_by</strong>, and a string named <strong style="user-select: auto;">tag_name</strong>. The task is to print a new string such that <strong style="user-select: auto;">tag_name </strong>is in the <strong style="user-select: auto;">middle </strong>of <strong style="user-select: auto;">bound_by</strong>.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></span></p>

<pre style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong> </span>
<span style="font-size: 18px; user-select: auto;">bound_by = [[]], tag_name = tag</span>
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Output:</strong></span>
<span style="font-size: 18px; user-select: auto;">[[tag]]<strong style="user-select: auto;">
</strong></span></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></span></p>

<pre style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Input:</strong> </span>
<span style="font-size: 18px; user-select: auto;">bound_by = &lt;&gt;, tag_name = body</span>
<span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Output:</strong>
&lt;body&gt;</span></pre>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Your Task:</strong><br style="user-select: auto;">
Your task is to complete the function&nbsp;<strong style="user-select: auto;">join_middle()</strong> which should <strong style="user-select: auto;">return </strong>the modified string.</span></p>

<p style="user-select: auto;"><span style="font-size: 18px; user-select: auto;"><strong style="user-select: auto;">Constraints:</strong><br style="user-select: auto;">
1 &lt;= |tag_name| &lt;= 10<sup style="user-select: auto;">3</sup></span></p>

<p style="user-select: auto;">&nbsp;</p>

<p style="user-select: auto;"><iframe frameborder="0" height="315" src="https://www.youtube.com/embed/i5WNg3UOkQk" width="560" style="user-select: auto;"></iframe></p>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python-strings</code>&nbsp;<code>python</code>&nbsp;