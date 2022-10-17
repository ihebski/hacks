<?php
function do_xor($a,$b) {
  $s = '';
  for ($i=0; $i < max(strlen($a),strlen($b)); $i++) {
    $x = $i < strlen($a) ? ord($a[$i]) : 0;
    $y = $i < strlen($b) ? ord($b[$i]) : 0;
    $s .= chr($x ^ $y);
  }
  return $s;
}
function hmac($algo,$a,$b){
	return hash_hmac($algo, $a, $b);
}
$flag = "XkZDRgdBVUtpCRZoBkBRaFBoLANKWGx1Vl4EBhdFHmIwYWY4OTI2N2FmNTU4MzE2ZWY0MWQ1OGRjMGQ2MDlhMw==";
echo "<pre> flag : ".do_xor(base64_decode($flag),hmac('sha256','admin',crypt('You_4r3_4_b4d_b0Y','123456')))."</pre>";
