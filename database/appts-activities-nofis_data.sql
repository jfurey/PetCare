INSERT INTO activity_logs (pet_id, activity_type, other_activity_type, duration_minutes, activity_date, notes)
VALUES 
(1, 'Walk', NULL, 30, '2025-04-27 08:30:00', 'Morning walk around the park. Very energetic.'),
(2, 'Play', NULL, 45, '2025-04-27 15:00:00', 'Played fetch and tug-of-war.'),
(8, 'Other', 'Swimming', 60, '2025-04-26 12:00:00', 'Took a swim at the dog-friendly beach.'),
(2, 'Run', NULL, 20, '2025-04-25 07:00:00', 'Quick run before breakfast.');
(4, 'Play', NULL, 20, '2025-04-27 18:00:00', 'Played with a laser pointer and feather toy.');

UPDATE appointments
SET pet_id = 8
WHERE appointment_id = 4;

INSERT INTO appointments (pet_id, contact_id, appointment_type, other_appt_type, appointment_date, appointment_time, notes)
VALUES
(2, 6, 'Veterinarian', NULL, '2025-05-01', '10:30:00', 'Annual checkup and vaccines.'),
(1, 2, 'Grooming', NULL, '2025-05-03', '14:00:00', 'Full grooming session (bath, haircut, nails).'),
(1, 3, 'Other', 'Therapy Session', '2025-05-05', '11:00:00', 'First therapy dog training assessment.'),
(3, 4, 'Training', NULL, '2025-05-06', '16:00:00', 'Obedience refresher course.');



-- Pet 1 (Primary owner: user_id = 1)
INSERT INTO notifications (user_id, pet_id, type, title, message, is_read)
VALUES
(1, 1, 'Medication Reminder',
 'Heartgard Plus Renewal Needed',
 'Heartgard Plus for Pet #1 ended on 2024-01-15. Please check with Dr. Sarah Williams for renewal.', FALSE),

(1, 1, 'Medication Reminder',
 'Rimadyl Course Completed',
 'Rimadyl for Pet #1 ended on 2023-03-20. Contact Dr. James Miller if further treatment is needed.', FALSE),

-- Pet 2 (Primary owner: user_id = 3)
(3, 2, 'Medication Reminder',
 'Frontline Plus Renewal Needed',
 'Frontline Plus for Pet #2 ended on 2023-12-01. Please renew monthly treatment if applicable.', FALSE),

(3, 2, 'Medication Reminder',
 'Apoquel Course Completed',
 'Apoquel for Pet #2 ended on 2023-04-05. Contact Dr. Sarah Johnson for a new prescription if needed.', FALSE),

-- Pet 3 (Primary owner: user_id = 5)
(5, 3, 'Medication Reminder',
 'Doxycycline Course Completed',
 'Doxycycline for Pet #3 ended on 2023-03-05. Confirm with Dr. James Miller if additional treatment is required.', FALSE),

-- Pet 4 (Primary owner: user_id = 6)
(6, 4, 'Medication Reminder',
 'Revolution Renewal Needed',
 'Revolution for Pet #4 ended on 2023-12-10. Please renew monthly application as needed.', FALSE),

(6, 4, 'Medication Reminder',
 'Amoxicillin Course Completed',
 'Amoxicillin for Pet #4 ended on 2023-03-29. Follow up with Dr. Sarah Williams if needed.', FALSE),

-- Pet 5 (Primary owner: user_id = 7)
(7, 5, 'Medication Reminder',
 'Melafix Course Completed',
 'Melafix for Pet #5 ended on 2023-03-07. Consider water treatment renewal if condition persists.', FALSE),

-- Pet 8 (Primary owner: user_id = 1)
(1, 8, 'Medication Reminder',
 'NexGard Renewal Needed',
 'NexGard for Pet #8 ended on 2024-02-15. Please continue monthly chewables for parasite prevention.', FALSE),

(1, 8, 'Medication Reminder',
 'Prednisone Course Completed',
 'Prednisone for Pet #8 ended on 2023-04-03. Consult Dr. Sarah Johnson before resuming.', FALSE);


-- Pet 1 (Primary owner: user_id = 1)
INSERT INTO notifications (user_id, pet_id, type, title, message, is_read)
VALUES
(1, 1, 'Appointment Reminder',
 'Veterinarian Appointment on 2025-04-10',
 'Your pet (ID: 1) has a veterinarian appointment on 2025-04-10 at 14:30. Notes: Annual check-up and vaccination.', FALSE),

(1, 1, 'Appointment Reminder',
 'Physical Therapy Appointment on 2025-04-15',
 'Your pet (ID: 1) has a Physical Therapy appointment on 2025-04-15 at 10:00. Notes: Post-surgery rehabilitation session.', FALSE),

(1, 1, 'Appointment Reminder',
 'Grooming Appointment on 2025-05-03',
 'Your pet (ID: 1) has a grooming appointment on 2025-05-03 at 14:00. Notes: Full grooming session (bath, haircut, nails).', FALSE),

(1, 1, 'Appointment Reminder',
 'Therapy Session on 2025-05-05',
 'Your pet (ID: 1) has a Therapy Session on 2025-05-05 at 11:00. Notes: First therapy dog training assessment.', FALSE),

-- Pet 2 (Primary owner: user_id = 3)
(3, 2, 'Appointment Reminder',
 'Veterinarian Appointment on 2025-05-01',
 'Your pet (ID: 2) has a veterinarian appointment on 2025-05-01 at 10:30. Notes: Annual checkup and vaccines.', FALSE),

-- Pet 3 (Primary owner: user_id = 5)
(5, 3, 'Appointment Reminder',
 'Training Appointment on 2025-05-06',
 'Your pet (ID: 3) has a training appointment on 2025-05-06 at 16:00. Notes: Obedience refresher course.', FALSE),

-- Pet 8 (Primary owner: user_id = 1)
(1, 8, 'Appointment Reminder',
 'Grooming Appointment on 2025-04-18',
 'Your pet (ID: 8) has a grooming appointment on 2025-04-18 at 15:45. Notes: Grooming session with bath, haircut, and nail trim.', FALSE);

-- Pet 1 (Primary owner: user_id = 1)
INSERT INTO notifications (user_id, pet_id, type, title, message, is_read)
VALUES
(1, 1, 'Vaccination Due',
 'Rabies Vaccine Overdue',
 'Rabies vaccine for Pet #1 was due on 2024-01-15. Please schedule with Dr. Sarah Williams.', FALSE),

(1, 1, 'Vaccination Due',
 'DHPP Vaccine Overdue',
 'DHPP vaccine for Pet #1 was due on 2024-02-10. Please schedule with Dr. Sarah Williams.', FALSE),

(1, 1, 'Vaccination Due',
 'Bordetella Vaccine Overdue',
 'Bordetella vaccine for Pet #1 was due on 2023-09-05. Please schedule with Dr. James Miller.', FALSE),

-- Pet 2 (Primary owner: user_id = 3)
(3, 2, 'Vaccination Due',
 'Rabies Vaccine Overdue',
 'Rabies vaccine for Pet #2 was due on 2024-01-20. Please schedule with Dr. Sarah Johnson.', FALSE),

(3, 2, 'Vaccination Due',
 'DHPP Vaccine Overdue',
 'DHPP vaccine for Pet #2 was due on 2024-01-20. Please schedule with Dr. Sarah Johnson.', FALSE),

(3, 2, 'Vaccination Due',
 'Leptospirosis Vaccine Overdue',
 'Leptospirosis vaccine for Pet #2 was due on 2024-01-20. Please schedule with Dr. Sarah Johnson.', FALSE),

-- Pet 4 (Primary owner: user_id = 6)
(6, 4, 'Vaccination Due',
 'Rabies Vaccine Overdue',
 'Rabies vaccine for Pet #4 was due on 2024-02-15. Please schedule with Dr. Sarah Williams.', FALSE),

(6, 4, 'Vaccination Due',
 'FVRCP Vaccine Overdue',
 'FVRCP vaccine for Pet #4 was due on 2024-02-15. Please schedule with Dr. Sarah Williams.', FALSE),

(6, 4, 'Vaccination Due',
 'FeLV Vaccine Overdue',
 'FeLV vaccine for Pet #4 was due on 2024-03-10. Please schedule with Dr. James Miller.', FALSE),

-- Pet 8 (Primary owner: user_id = 1)
(1, 8, 'Vaccination Due',
 'Rabies Vaccine Overdue',
 'Rabies vaccine for Pet #8 was due on 2024-03-01. Please schedule with Dr. Sarah Johnson.', FALSE),

(1, 8, 'Vaccination Due',
 'DHPP Vaccine Overdue',
 'DHPP vaccine for Pet #8 was due on 2024-03-01. Please schedule with Dr. Sarah Johnson.', FALSE);
