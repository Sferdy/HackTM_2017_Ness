using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
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

namespace HIB
{
    [Activity(Label = "Activity1")]
    public class Activity1 : Activity
    {
        
        protected async override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            SetContentView(Resource.Layout.Second);
            TextView[] tview = new TextView[10];
            tview[0] = FindViewById<TextView>(Resource.Id.textView10);
            tview[1] = FindViewById<TextView>(Resource.Id.textView11);
            tview[2] = FindViewById<TextView>(Resource.Id.textView12);
            tview[3] = FindViewById<TextView>(Resource.Id.textView13);
            tview[4] = FindViewById<TextView>(Resource.Id.textView14);
            tview[5] = FindViewById<TextView>(Resource.Id.textView15);
            tview[6] = FindViewById<TextView>(Resource.Id.textView16);
            tview[7] = FindViewById<TextView>(Resource.Id.textView17);
            tview[8] = FindViewById<TextView>(Resource.Id.textView18);



            var uniqueness = Intent.Extras.GetStringArrayList("uniqueness") ?? new string[0];

            int counter = 0;
            Color color = Color.LightGreen; 
            foreach(string unique in uniqueness)
            {
                if (counter < 8)
                {
                    tview[counter].Text = unique;

                    if (unique == "-1")
                    {
                        color = Color.Orange;
                    }
                    if (unique == "-10")
                    {
                        color = Color.Red;
                    }
                    if (unique == "0")
                    {
                        color = Color.LightGreen;
                    }
                    tview[counter].SetTextColor(color);
                    counter++;
                }
            }

        }



    }
}