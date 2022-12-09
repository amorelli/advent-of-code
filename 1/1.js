const elf = input => {
  const data = String(input).split("\n");

  let largest = 0;
  let compare = 0;

  for (let i = 0; i < data.length; i++) {
    if (data[i] === "") {
      if (compare > largest) {
        largest = compare;
      }
      compare = 0;
    } else {
      compare = compare + Number(data[i]);
    }
  }

  return largest;
};
