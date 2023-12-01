use std::fs;
use std::collections::HashMap;

fn main() {
    let file_path = "./input.txt";
    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    let coords = contents.lines();
    let mut number_hashmap = HashMap::new();
    let spelled_numbers = ["oneight", 
                            "twone",
                            "threeight",
                            "fiveight",
                            "sevenine",
                            "eightwo",
                            "eighthree",
                            "nineight",
                            "zerone",
                            "one",
                            "two",
                            "three",
                            "four",
                            "five",
                            "six",
                            "seven",
                            "eight",
                            "nine",
                            "zero"];
    let spelled_values = ["18",
                                    "21",
                                    "38",
                                    "58",
                                    "79",
                                    "82",
                                    "83",
                                    "98",
                                    "01",
                                    "1",
                                    "2",
                                    "3",
                                    "4",
                                    "5",
                                    "6",
                                    "7",
                                    "8",
                                    "9",
                                    "0"];
    let mut i = 0;
    for spelled_num in spelled_numbers {
        number_hashmap.insert(spelled_num, spelled_values[i]);
        i += 1;
    }        
              
    // let mut i = 0;
    let mut coord_array = Vec::new();
    for coord in coords {
        // println!("{coord}");
        let mut num_coord = String::from(coord);
        for key in spelled_numbers {
            num_coord = num_coord.replace(key, number_hashmap.get(&key).unwrap());
        }
        // println!("{num_coord}");
        let nums:Vec<&str> = num_coord.split(char::is_alphabetic).filter(|&x| !x.is_empty()).collect();
        let nums = nums.join("");
        let first = &nums[0..1];
        let last = &nums[nums.len()-1..nums.len()];
        let decoded_num = format!("{first}{last}").parse::<i32>().unwrap();
        coord_array.push(decoded_num);
        // println!("{:?}", spelled_nums);
        // i += 1;
        // if i == 10 {
        //     break;
        // }
        
        // let nums = nums.collect::<Vec<&str>>();
        // let first = nums[0];
        // let last = nums[nums.len()-1];
        // println!("First number: {first} last number: {last}");
    }
    let coord_sum: i32 = coord_array.iter().sum();
    println!("Coordinate sum:{coord_sum}");
}
