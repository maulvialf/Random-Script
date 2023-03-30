function rjust(str, length, char) {
  str = String(str);
  char = char || ' ';
  while (str.length < length) {
    str = char + str;
  }
  return str;
}

function ljust(str, length, char) {
  str = String(str);
  char = char || ' ';
  while (str.length < length) {
    str = str + char;
  }
  return str;
}
