# Challenge

This is a simple webservice for user query diet list.

##   Environment

*   python2.7
*   pandas
*   flask

Example:

To use webservice, the key and the value should follow the rules.

gender  : could be [Female/Male/F/M/f/m] <br> 
ages    : range 2 ~ 120

<pre>http://54.196.135.79/diet?gender=&lt;gender&gt;&ages=&lt;age&gt; </pre>

Or use command line to get the json result.

<pre>python balanced_diet.py -g &lt;gender&gt; -a &lt;age&gt; </pre>

