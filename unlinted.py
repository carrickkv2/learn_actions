def process_data(data, filter_criteria, sort_order, include_metadata, output_format, save_to_file, notify_user):
    print("Processing data with the following parameters: data={}, filter_criteria={}, sort_order={}, include_metadata={}, output_format={}, save_to_file={}, notify_user={}".format(
        data, filter_criteria, sort_order, include_metadata, output_format, save_to_file, notify_user))

def main():
    data = "sample_data"
    filter_criteria = "age > 30"
    sort_order = "ascending"
    include_metadata = True
    output_format = "json"
    save_to_file = False
    notify_user = True
    process_data(data, filter_criteria, sort_order, include_metadata, output_format, save_to_file, notify_user)

main()
