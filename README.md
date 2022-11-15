# Pitch_Identification
Identify a single clear note of the D-major Guzheng
<br>
<div style="text-align: center; margin-top: 2%;"><b>Guzheng note table</b></div>
<div><img src="static/Guzhengnotes_nowm.jpg" alt="Guzheng_picture" width="35%" style="margin-left: 2%; margin-top: 2%;"></div>


<h2 style="clear: both;">How I implemented this program</h2>
    <ul>
        <li>First using Fourier transformation to get the pitch spectrum, which is shown above.
            <ul>
                <li>A little explanation: the leftmost peak with a high prominence is usually the pitch of the note. This pattern could actually be easily seen with bare eyes. </li>
            </ul>
        </li>
        <li>Second using the peak detection algorithm to find the first peak with a high prominence. Done!</li>
        <ul>
            <li>I've tried other machine learning algorithms to identify the pattern. But later I found that a simple rule-based peak detection algorithm works best.</li>
        </ul></ul>

<h2 style="clear: both;">Pitch Spectrum of 21 notes (The leftmost peak with a high prominence is the pitch.)</h2>
<div class="box">
    <img src="static/1.jpg" alt="Note 1" width="23%">
    <img src="static/2.jpg" alt="Note 2" width="23%">
    <img src="static/3.jpg" alt="Note 3" width="23%">
    <img src="static/4.jpg" alt="Note 4" width="23%">
    <img src="static/5.jpg" alt="Note 5" width="23%">
    <img src="static/6.jpg" alt="Note 6" width="23%">
    <img src="static/7.jpg" alt="Note 7" width="23%">
    <img src="static/8.jpg" alt="Note 8" width="23%">
    <img src="static/9.jpg" alt="Note 9" width="23%">
    <img src="static/10.jpg" alt="Note 10" width="23%">
    <img src="static/11.jpg" alt="Note 11" width="23%">
    <img src="static/12.jpg" alt="Note 12" width="23%">
    <img src="static/13.jpg" alt="Note 13" width="23%">
    <img src="static/14.jpg" alt="Note 14" width="23%">
    <img src="static/15.jpg" alt="Note 15" width="23%">
    <img src="static/16.jpg" alt="Note 16" width="23%">
    <img src="static/17.jpg" alt="Note 17" width="23%">
    <img src="static/18.jpg" alt="Note 18" width="23%">
    <img src="static/19.jpg" alt="Note 19" width="23%">
    <img src="static/20.jpg" alt="Note 20" width="23%">
    <img src="static/21.jpg" alt="Note 21" width="23%">
 </div>
