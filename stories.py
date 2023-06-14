import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


def Stories():
    tab1, tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs(['story 1','story 2', 'story 3','story 4','story 5','story 6','story 7','story 8','story 9','story 10'])
    with tab1:
        st.subheader("story 1")
        st.write("Once upon a time, in the bustling halls of West Windsor-Plainsboro High School South (HSS), a new student named Raj arrived from India. Raj was an innocent and curious individual, eager to adapt to his new environment. Little did he know that his journey in this school would be filled with mystery and intrigue.")
        add_vertical_space()
        st.write("Walking down the hall to his first class, Raj almost bumped into someone.“Watch where you’re going dude!” the person he almost bumped into yells not unkindly.Bustling was definitely the right way to describe this place. Everyone moved about, knowing where to go and how to skillfully avoid accidents. Well, everyone except Raj. Although that probably had something to do with the fact that he was new.")
        add_vertical_space()
        st.write("Luckily, was starting to get the hang of the schedule. As Raj settled into his classes, he noticed two distinct personalities among his classmates. The first of these was Ram Panchangam, a highly intelligent and puzzle-loving student, who always seemed to be one step ahead in solving mysteries.")
        add_vertical_space()
        st.write("Raj had met Ram on his first day in his forensics class. Raj and Ram were assigned to sit next to each other. Raj shyly smiled at Ram, not sure how to approach a new person.")
        add_vertical_space()
        st.write("“Hey, I’ve never seen you around before. I’m Ram, what’s your name? Why did you take this class? I want to be a detective so that’s why I’m here, you know cause it would totally help me I’m sure!”")
        add_vertical_space()
        st.write("Well, it seemed as though Ram was the opposite, greeting Raj excitedly as though he wasn’t a complete stranger.")
        add_vertical_space()
        st.write("“Uh, I’m Raj. I just took it because I thought it would be cool. And um, good for you, the uh, detective stuff.” Raj responded, voice wavering a bit.")
        add_vertical_space()
        st.write("“It’s great to meet you Raj! I guess we’ll be partners for this marking period!” Ram responded enthusiastically.")
        add_vertical_space()
        st.write("Throughout the next few weeks, Raj and Ram got to learn about each other, like their strengths and weaknesses. Raj got more comfortable with Ram and opened up, earning each other as friends.")
        add_vertical_space()
        st.write("On the other hand, Raj met Trishna Shyamala, who had a malicious nature and took pleasure in causing problems for others, including Raj.")
        add_vertical_space()
        st.write("Raj had met Trishna on his second day, during gym class. Raj had always had good intuition so he knew something was off with Trishna. After his meeting with Ram, Raj’s confidence had improved a bit. So, he felt confident enough to introduce himself to the boy with a gym locker next to his before class started.")
        add_vertical_space()
        st.write("“Hi, I’m Raj. I’m new here,” Raj said, extending his hand.")
        add_vertical_space()
        st.write("“And I don’t care, newbie,” Trishna replied arrogantly, walking away, leaving a stunned Raj behind.")
        add_vertical_space()
        st.write("After that, Raj decided it might be best to stay away from Trishna. Unfortunately, that simply didn’t seem to be an option for him…")
        add_vertical_space()
        st.write("One day, Raj stumbled upon a peculiar painting in the school hallway. The painting depicted a compass pointing southeast, captivating his attention. Below the compass, a riddle was inscribed:")
        add_vertical_space()
        st.write('.. -. / ... -.-. .... --- --- .-.. --..-- / .- / .--. .- .. -. - .. -. --. / .-- .. - .... / -.-. --- -- .--. .- ... ... / -... --- .-.. -.. --..-- / .--. --- .. -. - ... / ... --- ..- - .... . .- ... - --..-- / .- / - .- .-.. . / - --- / ..- -. ..-. --- .-.. -.. .-.-.- / .-.. --- --- -.- / -... . .-.. --- .-- --..-- / .-- .... . .-. . / .--. .. .-. .- - . ... / .-. --- .- -- --..-- / .... --- .-- / -- .- -. -.-- / --. --- --- -.. / . -.-- . ... / -.-. .- .-.. .-.. / .. - / .... --- -- . ..--..')
        add_vertical_space()
        st.write(".- / .--. .. .-. .- - . / .- .-- .- .. - ... --..-- / .- / -.. .- .-. .. -. --. / ... .. --. .... - --..-- / -... ..- - / .... --- .-- / -- .- -. -.-- / . -.-- . ... / ... .... .. -. . / .-- .. - .... / .-.. .. --. .... - ..--.. ... . . -.- / - .... . / .- -. ... .-- . .-. --..-- / .-.. . - / -.-. ..- .-. .. --- ... .. - -.-- / --. ..- .. -.. . --..-- / - .... . / .--. .- .. -. - .. -. --. .----. ... / ... . -.-. .-. . - / .. - / ... .... .- .-.. .-.. / -.-. --- -. ..-. .. -.. . .-.-.-")
        a = st.text_input("what is the answer to this riddle1?")
        if a == '1':
            r_s=st.success("Riddle sloved")
            b_b=st.balloons()
            st.write("Intrigued by the riddle, Raj immediately sensed that solving it would lead him closer to the heart of the mystery surrounding the school. With determination in his eyes, he sought the help of Ram Panchangam, who had a reputation for being skilled at puzzles.")
            add_vertical_space()
            st.write("“Hey Ram, I have to ask you something,” Raj said, sitting down at their lunch table.")
            add_vertical_space()
            st.write("“Of course Raj, what’s up dude?” Ram said, once they finished chewing their food.")
            add_vertical_space()
            st.write("“So you know how you’re good at solving puzzles and you want to be a detective and all,” Raj continues once Ram nods. “There’s this painting in the hallway with a compass on it. There’s what looks like a riddle underneath. I was wondering if you would help me solve it?”")
            add_vertical_space()
            st.write("“Sure dude, I would love to! Let’s eat and then I’ll see if I can work my magic,” Ram replied eagerly. “But dude, I have to warn you about Trishna.”")
            add_vertical_space()
            st.write("“Who’s that?”")
            add_vertical_space()
            st.write("“He’s right there actually,” Ram whispers, pointing. Following their finger, Raj realizes that Trishna was also the guy who was rude to him in gym class.")
            add_vertical_space()
            st.write("“Oh I know him. He was quite rude.”")
            add_vertical_space()
            st.write("“He has a habit of going out of his way to cause problems for everyone.” Ram warned.")
            add_vertical_space()
            st.write("Ram then joined Raj in deciphering the riddle. They examined the painting closely, noting the details of the compass pointing southeast. Ram's sharp mind quickly realized that 'below' referred to a lower part of the school building, where the art classes were held. They followed the clue and arrived at the art room.")
            add_vertical_space()
            st.write("Inside the art room, they discovered a large mural of a pirate ship sailing through stormy seas. Amongst the chaos, they noticed several pairs of glowing eyes amidst the darkness. Raj and Ram counted the eyes, carefully examining each part of the mural. After a meticulous count, they arrived at the answer: seven pairs of eyes.")
            add_vertical_space()
            st.write("“Ram, we figured it out!” Raj exclaimed.")
            add_vertical_space()
            st.write("“Firstly, we’re not done, and secondly, keep it down! You don’t want Trishna to show up!” Ram shushed.")
            add_vertical_space()
            st.write("“Oh sorry dude.” Raj responded, looking around. “I guess we just work in secret to find out what the hidden message is.”")
            add_vertical_space()
            st.write("Ram nodded and the duo revisited the original riddle, pondering its meaning.")
            add_vertical_space()
            st.write("“Wait, I think the ‘glowing eyes’ might just be stars. This kind of looks like a constellation,” Raj said, eyes growing wide.")
            add_vertical_space()
            st.write("“Oh you might be right! That kind of looks like Orion, the hunter,  now that you mention it,” Ram added. They had figured out the next important piece of the puzzle.")
            add_vertical_space()
            st.write("Excitement coursing through their veins, Raj and Ram searched for clues related to Orion. They soon discovered a hidden compartment behind the mural, which contained a map leading to a buried treasure within the school grounds.")
            add_vertical_space()
            st.write("Together, they embarked on a thrilling adventure, following the clues on the map. They solved puzzles, navigated through secret passages, and overcame challenges along the way. With each step, their bond grew stronger, and they became an unstoppable duo. Try as he might, Trishna failed to trip them up no matter how.")
            add_vertical_space()
            st.write("Finally, they reached the designated spot on the map, where they unearthed a chest filled with ancient artifacts and treasures.")
            add_vertical_space()
            st.write("“Ram, now we got it for sure!” Raj exclaimed, practically vibrating where he stood.")
            add_vertical_space()
            st.write("“Yea I think we do,” Ram replied calmly for once. Oh how the turntables in their attitudes.")
            add_vertical_space()
            st.write("Their discovery not only solved the mystery surrounding the painting but also revealed the rich history of the school.")
            add_vertical_space()
            st.write("Raj and Ram were hailed as heroes, celebrated for their wit and perseverance. Trishna Shyamala, realizing his attempts to sabotage their efforts had failed, slinked away in defeat.")
            add_vertical_space()
            st.write("As Raj and Ram returned to their everyday lives at HSS, they cherished the memories they had forged together and continued to solve mysteries that came their way. For example, one time someone asked them to find their lost necklace.")
            add_vertical_space()
            st.write("“Ram, Raj, I lost my necklace, will you please help me find it?” someone asked.")
            add_vertical_space()
            st.write("“We’ll do it,” Ram replied, once both Ram and Raj had nodded at each other.")
            add_vertical_space()
            st.write("They had found out someone had stolen it and made sure to return the necklace to the rightful owner. Their remarkable journey had not only unveiled the secrets of the school but also solidified a friendship that would last a lifetime.")
            add_vertical_space()
            st.write("Word of their adventure quickly spread throughout West Windsor-Plainsboro High School South, capturing the imagination of their fellow students. Inspired by Raj and Ram's bravery and intellect, many students formed their own detective clubs and began unraveling their own mysteries within the school.")
            add_vertical_space()
            st.write("Raj and Ram gladly shared their expertise, offering guidance and mentoring to the newfound detectives. They became a source of inspiration, encouraging their peers to embrace their curiosity and think outside the box. The school's atmosphere transformed into a hub of excitement and exploration, with students eagerly searching for hidden secrets and puzzles.")
            add_vertical_space()
            st.write("As time went on, Raj and Ram became known as the dynamic duo of HSS. Their reputation grew not only within the school but also in the wider community. Local newspapers featured articles about their adventures, and they were even invited to give talks and workshops on problem-solving and critical thinking.")
            add_vertical_space()
            st.write("The school administration recognized the positive impact Raj and Ram had on the student body and decided to create an annual 'Mystery Week' event. ")
            add_vertical_space()
            st.write("“Attention students, next week is our first annual ‘Mystery Week’ event. During this week, the entire school will be transformed into an interactive puzzle-filled playground. Clues will be hidden in lockers, classrooms, and even in the cafeteria, challenging students to solve intricate riddles and codes. All students are encouraged to participate.” a voice spoke over the intercom. “Ram Panchangam and Raj Talvaar, please come to the office.”")
            add_vertical_space()
            st.write("“As our dynamic duo, we want both of you to design the grand mystery at the end of ‘Mystery Week’. Would you both be interested in doing so?” a member of the administration asked, once both Ram and Raj were seated.")
            add_vertical_space()
            st.write("The two looked at each other as though they had a silent conversation without needing to speak. Looking back over, Raj started, “We would love to!”")
            add_vertical_space()
            st.write("“It would be so cool for us to do that,” Ram added, eyes shining at the prospect of being put in charge of something like this.")
            add_vertical_space()
            st.write("“We’re glad you both agreed. Brainstorm tonight, and let’s meet during your lunch tomorrow”")
            add_vertical_space()
            st.write("Raj and Ram were given the honor of designing the grand finale mystery, a tradition that would continue year after year. The school community eagerly awaited Mystery Week, knowing that it would be an exhilarating and mind-bending experience.")
            add_vertical_space()
            st.write("Beyond their adventures, Raj and Ram excelled academically. They continued to impress their teachers with their sharp intellect and problem-solving skills.")
            add_vertical_space()
            st.write("Years later, as they prepared to graduate from high school, Raj and Ram reflected on their incredible journey. Raj discovered a passion for physics, while Ram's interest in puzzles led him to pursue a career in game design. They realized that their time at HSS had not only shaped their own lives but had also impacted the lives of their classmates. The spirit of curiosity and exploration they had ignited continued to thrive within the school, fostering a community of lifelong learners.")
            add_vertical_space()
            st.write("As they bid farewell to West Windsor-Plainsboro High School South, Raj and Ram knew that their friendship and shared love for mysteries would endure. They were excited to embark on new adventures and solve even greater puzzles, knowing that they could overcome any challenge with their bond and unwavering determination.")
            add_vertical_space()
            with tab2:
                st.write("Kamala Veda, a bright and ambitious student, found herself caught up in a web of mystery and intrigue at West Windsor-Plainsboro High School South (HSS). It was her second year at the school since moving from India, and she had set her sights on outshining her classmates, especially Ethan Shenke, the brilliant student known for his prowess in Advanced Placement classes.")
                add_vertical_space()
                st.write("Little did Kamala know, Ethan harbored his own aspirations of becoming a lawyer or a politician. He possessed a sharp mind and a knack for solving puzzles and mysteries. When Kamala found herself faced with a series of enigmatic challenges, it was Ethan who offered his help, eager to prove his intellectual prowess.")
                add_vertical_space()
                st.write("Meanwhile, there was Benjamin Young, a troublemaker who took pleasure in causing problems for Kamala. He seemed to revel in the chaos he created, always seeking to undermine her efforts and hinder her progress. But Kamala was undeterred, determined to overcome the obstacles thrown her way.")
                add_vertical_space()
                st.write("One day, while exploring the school's art gallery, Kamala stumbled upon a peculiar painting. It featured a door, and beneath it, the number '600' was inscribed. Intrigued, she examined the painting more closely. On either side of the door's hands were carefully arranged words. It was then she noticed a small verse, seemingly a clue to unravel the mystery.")
                add_vertical_space()
                st.write("SW4gYSBwYWludGluZydzIGdhemUsIGEgZG9vciBpdCBzcGllcywKV2l0aCB0aGUgbmFtZSAnNjAwJyB0byB5b3VyIHN1cnByaXNlLgpCZXNpZGUgdGhlIGhhbmRzLCB3b3JkcyBuZWF0bHkgYWRvcm4sCk5vdyBjb2xsZWN0IHRoZSBmaXJzdCBsZXR0ZXJzLCB5b3VyIHRhc2sgaXMgYm9ybi4K")
                add_vertical_space()
                st.write("U2VlayB0aGUgYW5zd2VyIHdpdGhpbiB0aGlzIGNvZGVkIHNpZ24sCldoZXJlIGVhY2ggd29yZCdzIGZpcnN0IGxldHRlciBhbGlnbnMuCkRlY2lwaGVyIHRoZSByaWRkbGUsIHVubG9jayB0aGUgY2x1ZSwKRGlzY292ZXIgdGhlIG1lYW5pbmcgaGlkZGVuIGZyb20gdmlldy4KCg==")
                b = st.text_input("what is the answer to this riddle2?")
                if b == 'cnpup':
                    r_s
                    b_b
                    st.write("Kamala pondered over the lines, feeling a sense of urgency to decipher their meaning. She turned to Ethan, knowing that his analytical mind would prove invaluable in solving this intricate puzzle.")
                    add_vertical_space()
                    st.write("\"Ethan, can you help me figure out what this poem means? I think it's a clue to something important,\" Kamala requested, her eyes filled with determination.")
                    add_vertical_space()
                    st.write("Ethan's eyes lit up with excitement. \"Of course, Kamala. Let's break it down together. The first part mentions a door with the number '600.' Perhaps we should start by locating something related to that number in the school,\" he suggested.")
                    add_vertical_space()
                    st.write("As they explored the school grounds, they stumbled upon a locker bearing the number 600. It was locked, but Kamala recalled the second part of the poem, focusing on the first letters of the words. \"Each word's first letter aligns...,\" she murmured, tracing her finger across the poem.")
                    add_vertical_space()
                    st.write("Inspired by the idea, they carefully noted the first letter of each word beside the hands in the painting: I, a, d, t, h, n, b, n, l, y, t, i, y, t, i, f, l, y, t, b, t, f, l, u, c, d, t, m, h, v.")
                    add_vertical_space()
                    st.write("The letters seemed jumbled and disorganized, but Kamala had a hunch. \"I think these letters might form another clue, Ethan. Let's rearrange them and see if it leads us anywhere.\"")
                    add_vertical_space()
                    st.write("They rearranged the letters, and suddenly, the hidden message became clear. \"In a cold, dimly lit basement, near the lockers, you'll find...\"")
                    add_vertical_space()
                    st.write("Before Kamala could finish reading the message aloud, a shadowy figure emerged from the corner. It was Benjamin Young, wearing a wicked grin on his face. \"Well, well, well, what do we have here? Looks like you two are getting close to solving the mystery,\" he taunted.")
                    add_vertical_space()
                    st.write("Kamala's heart raced, but she refused to back down. \"Benjamin, why are you doing this? What do you gain from causing trouble?\"")
                    add_vertical_space()
                    st.write("\"I enjoy watching people struggle, Kamala. It brings me joy to see you all squirm,\" Benjamin sneered. \"But I suppose I can give you a hint, just to make things more interesting.\"")
                    add_vertical_space()
                    st.write("With an air of superiority, Benjamin handed Kamala a torn piece of paper. On it, there was a sentence that read, \"The key lies within knowledge.\"")
                    add_vertical_space()
                    st.write("As Kamala examined the torn piece, she realized that the clue pointed towards the school's library. She turned to Ethan, determination burning in her eyes.")
                    add_vertical_space()
                    st.write("\"We won't let Benjamin stop us, Ethan. We'll find the answers and put an end to this mystery once and for all,\" Kamala declared.")
                    add_vertical_space()
                    st.write("With renewed determination, Kamala and Ethan raced to the school library, ready to uncover the secrets that lay hidden within its shelves. Together, they delved into books and scoured through the vast collection, searching for any clue that would lead them closer to the truth.")
                    add_vertical_space()
                    st.write("As they continued their investigation, Kamala couldn't help but feel a mix of emotions. She had always competed with Ethan, driven by a desire to prove herself, but deep down, she realized that her feelings for him had grown into something more profound. She cherished their moments together, the way he encouraged her and supported her every step of the way.")
                    add_vertical_space()
                    st.write("Amidst the riddles and challenges they faced, Kamala and Ethan's bond grew stronger, and they discovered that working together was the key to unraveling the mystery that plagued their school.")
                    add_vertical_space()
                    st.write("The story of mystery and intrigue at West Windsor-Plainsboro High School South (HSS) would continue to unfold, as Kamala, Ethan, and their allies embarked on a journey of discovery, uncovering the truth hidden beneath the surface. And as they pursued the answers, Kamala hoped that one day she would find the courage to reveal her true feelings to Ethan, the one person who had always been by her side, supporting her through it all.")
                    add_vertical_space()
                    st.write("With the torn piece of paper pointing them towards the school library, Kamala and Ethan hurriedly made their way through the corridors, their hearts pounding with anticipation. As they entered the library, the scent of old books filled the air, creating an atmosphere of both familiarity and intrigue.")
                    add_vertical_space()
                    st.write("The librarian, Mrs. Desmond, greeted them with a warm smile. She had witnessed their determination and sensed their eagerness to uncover the secrets hidden within the library's vast collection. Mrs. Desmond had always been fascinated by the students' thirst for knowledge and their relentless pursuit of answers.")
                    add_vertical_space()
                    st.write("\"Can I help you two find something specific?\" Mrs. Desmond inquired, her voice gentle yet filled with curiosity.")
                    add_vertical_space()
                    st.write("Kamala showed her the torn piece of paper and explained their quest to solve the mystery that had enveloped the school. Mrs. Desmond's eyes sparkled with interest as she listened intently.")
                    add_vertical_space()
                    st.write("\"Well, my dear, you're in the right place,\" Mrs. Desmond replied. \"The library holds countless stories and hidden knowledge. Let's see what we can find together.\"")
                    add_vertical_space()
                    st.write("Guided by Mrs. Desmond's expertise, Kamala and Ethan combed through the shelves, scouring books on history, mythology, and cryptography. The library seemed to come alive with their excitement, as if the books themselves were eager to reveal their secrets.")
                    add_vertical_space()
                    st.write("Suddenly, Ethan's fingers grazed the spine of an old, weathered book, and a faint light illuminated his eyes. He pulled it from the shelf, and the title read, \"Secrets of the Enigmatic.\"")
                    add_vertical_space()
                    st.write("Kamala's heart quickened as they opened the book, revealing pages filled with cryptic symbols, mysterious illustrations, and stories of hidden treasures and unsolved mysteries.")
                    add_vertical_space()
                    st.write("As they delved into the book's contents, they discovered references to a secret chamber beneath the school—an underground labyrinth rumored to hold the answers to long-forgotten enigmas. It was said that only those who possessed a true thirst for knowledge and a resilient spirit could navigate its treacherous paths.")
                    add_vertical_space()
                    st.write("Kamala and Ethan realized that their journey had just begun. With the knowledge gained from the book, they deciphered a series of clues and symbols that pointed them toward the entrance of the secret chamber.")
                    add_vertical_space()
                    st.write("Late one evening, when the school was empty and bathed in an eerie silence, Kamala and Ethan found themselves standing before a heavy, ornate door concealed behind a bookcase in the library's restricted section. They exchanged a determined look, their hearts filled with anticipation and a touch of trepidation.")
                    add_vertical_space()
                    st.write("Together, they pushed the bookcase aside, revealing the hidden entrance. With bated breath, they stepped into the darkness, armed with their wits and the knowledge they had acquired.")
                    add_vertical_space()
                    st.write("As they ventured deeper into the secret chamber, the air grew colder, and whispers of forgotten tales echoed in the shadows. They encountered various challenges, including intricate puzzles, hidden compartments, and ancient artifacts that required careful examination.")
                    add_vertical_space()
                    st.write("Their teamwork and shared intellect proved invaluable as they deciphered each obstacle, inching closer to the heart of the mystery. With each step, Kamala admired Ethan's brilliance and dedication, realizing that he was not just a rival but also a trusted companion.")
                    add_vertical_space()
                    st.write("Finally, in the heart of the chamber, they discovered an ancient tome, its pages worn and fragile. Within its hallowed passages, they found the answers they had sought—the truth that would unravel the mystery haunting their school.")
                    add_vertical_space()
                    st.write("But as they prepared to leave the chamber, a figure emerged from the shadows. It was Benjamin Young, his malevolent grin now replaced with a look of desperation.")
                    add_vertical_space()
                    st.write("\"You thought you could solve the mystery without me,\" Benjamin spat, his voice tinged with bitterness. \"But you're not the only ones who deserve the answers. I've been searching for the truth as well.\"")
                    add_vertical_space()
                    st.write("Kamala and Ethan exchanged a glance, understanding the depth of Benjamin's desperation. They realized that beneath his mischievous nature, he, too, longed for the thrill of discovery and the satisfaction of unraveling the enigma that had captivated them all.")
                    add_vertical_space()
                    st.write("With empathy in her voice, Kamala spoke, \"Benjamin, we don't have to be adversaries in this. We can work together, share the knowledge we've gained, and find a way to bring the truth to light.\"")
                    add_vertical_space()
                    st.write("Benjamin hesitated for a moment, his eyes filled with conflict. Finally, he nodded, his guard slowly lowering. \"Alright, I'll trust you—for now. But don't think this means we're friends.\"")
                    add_vertical_space()
                    st.write("And so, Kamala, Ethan, and Benjamin forged an unlikely alliance, pooling their knowledge and skills to uncover the final pieces of the puzzle. As they pieced together the remaining clues, the mystery that had plagued West Windsor-Plainsboro High School South (HSS) began to unravel, revealing a web of corruption, hidden agendas, and secrets that threatened the integrity of the school itself.")
                    add_vertical_space()
                    st.write("Their journey was not without danger and unexpected twists, but their determination remained unwavering. With their combined efforts, they exposed the truth, exposing those responsible for the web of intrigue that had ensnared their beloved school.")
                    add_vertical_space()
                    st.write("As the dust settled and the truth came to light, Kamala and Ethan stood side by side, their bond forged through adversity. In that moment, Kamala found the courage to share her true feelings with Ethan, expressing her admiration and affection for him.")
                    add_vertical_space()
                    st.write("Ethan's eyes widened in surprise, his face breaking into a smile. \"Kamala, I've always admired your intelligence and determination. I feel the same way about you.\"")
                    add_vertical_space()
                    st.write("With the mystery solved and their hearts aligned, Kamala and Ethan stepped out of the secret chamber, ready to face a new chapter in their lives. They became known as the heroes who had brought justice to their school, and their story would be told for years to come.")
                    add_vertical_space()
                    st.write("United by their shared experiences, Kamala, Ethan, and Benjamin emerged as a formidable team, forever changed by their journey of discovery. Their friendship continued to thrive as they tackled new challenges, using their talents to make a positive impact on the world around them.")
                    add_vertical_space()
                    st.write("And as they walked hand in hand, Kamala and Ethan knew that their love for each other would forever be intertwined with the memories of their extraordinary adventure—the story that began with a web of mystery and ended with the triumph of truth, friendship, and the power of the human spirit.")
                    with tab3:
                        st.write("Shylock Oleksandr, a student at West Windsor-Plainsboro High School South (HSS), had always been fascinated by mysteries and detective stories. Ever since he came from Morocco to the United States in 10th grade, he had dreamt of becoming a real-life Shylock Holmes. With his keen observation skills and sharp mind, he was determined to solve the enigmas that crossed his path.")
                        add_vertical_space()
                        st.write("One day, while walking through the school corridors, Shylock stumbled upon a peculiar note. It read:")
                        add_vertical_space()
                        st.write("A%20compass%20pointing%20steadfast%20south%2C%0AGuiding%20travelers%20with%20silent%20mouth.%0AWhen%20facing%20its%20front%2C%20behold%20the%20sight%2C%0AA%20compass%20revealed%2C%20glowing%20with%20light.%0A%0A")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()
                        st.write("")
                        add_vertical_space()

