using Android.App;
using Android.Widget;
using Android.OS;
using System.Json;
using System.Threading.Tasks;
using System.Net;
using System.IO;
using System;
using Android.Graphics;
using Android.Content;
using System.Collections.Generic;

namespace HIB
{
    [Activity(Label = "HIB Application", MainLauncher = true, Icon = "@drawable/icon")]

    public class MainActivity : Activity
    {
        protected override void OnCreate(Bundle bundle)
        {
            base.OnCreate(bundle);

            // Set our view from the "main" layout resource
            SetContentView(Resource.Layout.Main);


            Button b = FindViewById<Button>(Resource.Id.button1);
           // Button routeHistoryButton = FindViewById<Button>(Resource.Id.routeHistoryButton);
            b.Click += async (sender, e) =>
            {
                // thingspeak cloud service unique url 
                // todo for current id
                string url = "https://api.thingspeak.com/channels/279003/feeds.json?api_key=4XS8082J7CIYESE7";

                // Fetch the weather information asynchronously, 
                // parse the results, then update the screen:
                JsonValue json = await FetchData(url);
                ParseAndDisplay(json);
            };

        }


        private async Task<JsonValue> FetchData(string url)
        {
            HttpWebRequest request = (HttpWebRequest)HttpWebRequest.Create(new Uri(url));
            request.ContentType = "application/json";
            request.Method = "GET";

            using (WebResponse response = await request.GetResponseAsync())
            {
                using (Stream stream = response.GetResponseStream())
                {
                    // Use this stream to build a JSON document object:
                    JsonValue jsonDoc = await Task.Run(() => JsonObject.Load(stream));
                    Console.Out.WriteLine("Response: {0}", jsonDoc.ToString());

                    return jsonDoc;
                }
            }

          
        }



        private void ParseAndDisplay(JsonValue json)
        {
            Button b2 = FindViewById<Button>(Resource.Id.button2);
            List<string> uniqueness = new List<string>();

            /* TextView t1 = FindViewById<TextView>(Resource.Id.textView1);
             TextView t2 = FindViewById<TextView>(Resource.Id.textView2);
             TextView t3 = FindViewById<TextView>(Resource.Id.textView3);
             TextView t4 = FindViewById<TextView>(Resource.Id.textView4);*/

            // feeds is what we want
            JsonValue feeds = json["feeds"];

            int? field1 = null;

            //hard breaking
            int proc1 = 100;
            string color = null;

            foreach (JsonValue feed in feeds)
            {
                color = feed["field1"];
                if (color != null)
                {
                    if (color.ToString() == "green")
                    {
                        // is ok
                        uniqueness.Add("0");

                    }

                    if (color.ToString() == "orange")
                    {
                        proc1 -= 1;
                        uniqueness.Add("-1");
                    }

                    if (color.ToString() == "red")
                    {
                        proc1 -= 10;
                        uniqueness.Add("-10");
                    }
                }
            }


            if(proc1 < 40)
            {
                b2.Text = "E";
                b2.SetBackgroundColor(Color.DarkRed);
            }
            else if(proc1 < 60)
            {
                b2.Text = "D";
                b2.SetBackgroundColor(Color.Orange);
            }
            else if (proc1 < 80)
            {
                b2.Text = "C";
                b2.SetBackgroundColor(Color.Blue);
            }
            else if (proc1 < 90)
            {
                b2.Text = "B";
                b2.SetBackgroundColor(Color.LightBlue);
            }
            else if (proc1 < 101)
            {
                b2.Text = "A";
                b2.SetBackgroundColor(Color.LightGreen);
            }


            b2.Click += (sender, e) =>
            {
                var intent = new Intent(this, typeof(Activity1));
                intent.PutStringArrayListExtra("uniqueness", uniqueness);
                StartActivity(intent);
            };




        }


        public int? ConvertToNumber(JsonValue jv)
        {
            int outValue;
            return int.TryParse((string)jv, out outValue) ? (int?)outValue : null;
        }
    }
}

