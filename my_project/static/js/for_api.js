const api_url = "http://127.0.0.1:8000/api/students/";
async function getStudent() {

      const response = await fetch(api_url);
      const data = await response.json();

      for (let i=0; i<data.length; i++) {
          $('#course').append("<td>" + data[i].course.name + "</td>");
          $('#name').append("<td>" + data[i].name + "</td>");
          $('#age').append("<td>" + data[i].age + "</td>");
          $('#email').append("<td>" + data[i].email + "</td>");
      }
    }

getStudent();