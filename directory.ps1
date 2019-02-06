get-childitem *.txt | foreach { 
    $string = $_.Name
    $a,$b = $string.split('-')
    $c='replaced'
    rename-item $_ "$a$c$b"
}