-- Medications for Max (Dog - Golden Retriever)
INSERT INTO medications (pet_id, medication_name, dosage, frequency, start_date, end_date, prescribed_by, created_at) VALUES
(1, 'Heartgard Plus', '1 chewable tablet', 'Monthly', '2023-01-15', '2024-01-15', 'Dr. Sarah Williams', NOW()),
(1, 'Rimadyl', '75mg', 'Twice daily', '2023-03-10', '2023-03-20', 'Dr. James Miller', NOW());

-- Medications for Bella (Dog - Labrador)
INSERT INTO medications (pet_id, medication_name, dosage, frequency, start_date, end_date, prescribed_by, created_at) VALUES
(2, 'Frontline Plus', '1 application', 'Monthly', '2023-02-01', '2023-12-01', 'Dr. Sarah Williams', NOW()),
(2, 'Apoquel', '16mg', 'Once daily', '2023-03-05', '2023-04-05', 'Dr. Sarah Johnson', NOW());

-- Medications for Oliver (Bird - Cockatiel)
INSERT INTO medications (pet_id, medication_name, dosage, frequency, start_date, end_date, prescribed_by, created_at) VALUES
(3, 'Doxycycline', '0.2ml', 'Twice daily', '2023-02-20', '2023-03-05', 'Dr. James Miller', NOW());

-- Medications for Luna (Cat - Maine Coon)
INSERT INTO medications (pet_id, medication_name, dosage, frequency, start_date, end_date, prescribed_by, created_at) VALUES
(4, 'Revolution', '1 application', 'Monthly', '2023-01-10', '2023-12-10', 'Dr. Sarah Johnson', NOW()),
(4, 'Amoxicillin', '50mg', 'Twice daily', '2023-03-15', '2023-03-29', 'Dr. Sarah Williams', NOW());

-- Medications for Bubbles (Fish - Goldfish)
INSERT INTO medications (pet_id, medication_name, dosage, frequency, start_date, end_date, prescribed_by, created_at) VALUES
(5, 'Melafix', '5ml per gallon', 'Daily water treatment', '2023-03-01', '2023-03-07', 'Dr. James Miller', NOW());

-- Medications for Buddy (Dog - Beagle)
INSERT INTO medications (pet_id, medication_name, dosage, frequency, start_date, end_date, prescribed_by, created_at) VALUES
(8, 'NexGard', '1 chewable tablet', 'Monthly', '2023-02-15', '2024-02-15', 'Dr. Sarah Williams', NOW()),
(8, 'Prednisone', '10mg', 'Once daily', '2023-03-20', '2023-04-03', 'Dr. Sarah Johnson', NOW());